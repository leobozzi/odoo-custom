# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

import uuid
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.tools.translate import _
from odoo.exceptions import Warning

import json
import logging
from werkzeug.exceptions import Forbidden

from odoo import http, SUPERUSER_ID ,tools, _
from odoo.http import request
from odoo.addons.base.models.ir_qweb_fields import nl2br
from odoo.addons.website.controllers.main import QueryURL
from odoo.exceptions import ValidationError


class sale_order(models.Model):
    _inherit = "sale.order"

    @api.depends('order_line.price_total','voucher_code')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        res = super(sale_order, self)._amount_all()
        for order in self:
            if order.voucher_code:
                amount_voucher = 0.0
                amount = self.env['gift.voucher'].search([('name','=', order.voucher_code)]).amount
                voucher_amount = amount
                if voucher_amount >= order.amount_total:
                    order.update ({
                                   'amount_voucher': voucher_amount,
                                    'amount_total': 0.0
                                   })
                else:
                    order.update({
                                  'amount_voucher': voucher_amount,
                                  'amount_total': order.amount_total - voucher_amount,
                                  })
            else:
                amount_untaxed = amount_tax = 0.0
                for line in order.order_line:
                    amount_untaxed += line.price_subtotal
                    amount_tax += line.price_tax
                if order.pricelist_id.currency_id:
                    order.update({
                        'amount_untaxed': order.pricelist_id.currency_id.round(amount_untaxed),
                        'amount_tax': order.pricelist_id.currency_id.round(amount_tax),
                        'amount_total': amount_untaxed + amount_tax,
                    })
                else:
                    order.update({
                        'amount_total': amount_untaxed + amount_tax,
                    })

    
    def _assign_voucher_code(self, code):
        self.ensure_one()
        self.update({
            'voucher_code' : code
            })
        return

    message = fields.Text('Message') # Add Custom Message in cart page
    amount_voucher = fields.Monetary(string='Voucher', store=True, readonly=True, compute='_amount_all', track_visibility='always')
    voucher_code = fields.Char(string='Voucher Code')
    
    
class website(models.Model):
    _inherit = "website"    
    
    
    def sale_get_order(self, force_create=False, code=None , code2=None, update_pricelist=False, force_pricelist=False):
        """ Return the current sale order after mofications specified by params.
        :param bool force_create: Create sale order if not already existing
        :param str code: Code to force a pricelist (promo code)
                         If empty, it's a special case to reset the pricelist with the first available else the default.
        :param bool update_pricelist: Force to recompute all the lines from sale order to adapt the price with the current pricelist.
        :param int force_pricelist: pricelist_id - if set,  we change the pricelist with this one
        :returns: browse record for the current sale order
        """
        self.ensure_one()
        partner = self.env.user.partner_id
        sale_order_id = request.session.get('sale_order_id')
        if not sale_order_id:
            last_order = partner.last_website_so_id
            available_pricelists = self.get_pricelist_available()
            # Do not reload the cart of this user last visit if the cart is no longer draft or uses a pricelist no longer available.
            sale_order_id = last_order.state == 'draft' and last_order.pricelist_id in available_pricelists and last_order.id

        pricelist_id = request.session.get('website_sale_current_pl') or self.get_current_pricelist().id

        if self.env['product.pricelist'].browse(force_pricelist).exists():
            pricelist_id = force_pricelist
            request.session['website_sale_current_pl'] = pricelist_id
            update_pricelist = True

        if not self._context.get('pricelist'):
            self = self.with_context(pricelist=pricelist_id)

        # Test validity of the sale_order_id
        sale_order = self.env['sale.order'].sudo().browse(sale_order_id).exists() if sale_order_id else None

        # create so if needed
        if not sale_order and (force_create or code):
            # TODO cache partner_id session
            pricelist = self.env['product.pricelist'].browse(pricelist_id).sudo()
            so_data = self._prepare_sale_order_values(partner, pricelist)
            so_data.update({
                            'voucher_code':code
                            })
            sale_order = self.env['sale.order'].sudo().create(so_data)

            # set fiscal position
            if request.website.partner_id.id != partner.id:
                sale_order.onchange_partner_shipping_id()
            else: # For public user, fiscal position based on geolocation
                country_code = request.session['geoip'].get('country_code')
                if country_code:
                    country_id = request.env['res.country'].search([('code', '=', country_code)], limit=1).id
                    fp_id = request.env['account.fiscal.position'].sudo()._get_fpos_by_region(country_id)
                    sale_order.fiscal_position_id = fp_id
                else:
                    # if no geolocation, use the public user fp
                    sale_order.onchange_partner_shipping_id()

            request.session['sale_order_id'] = sale_order.id

            if request.website.partner_id.id != partner.id:
                partner.write({'last_website_so_id': sale_order.id})

        if sale_order:

            # check for change of pricelist with a coupon
            pricelist_id = pricelist_id or partner.property_product_pricelist.id

            # check for change of partner_id ie after signup
            if sale_order.partner_id.id != partner.id and request.website.partner_id.id != partner.id:
                flag_pricelist = False
                if pricelist_id != sale_order.pricelist_id.id:
                    flag_pricelist = True
                fiscal_position = sale_order.fiscal_position_id.id

                # change the partner, and trigger the onchange
                sale_order.write({'partner_id': partner.id})
                sale_order.onchange_partner_id()
                sale_order.onchange_partner_shipping_id() # fiscal position
                sale_order['payment_term_id'] = self.sale_get_payment_term(partner)

                # check the pricelist : update it if the pricelist is not the 'forced' one
                values = {}
                if sale_order.pricelist_id:
                    if sale_order.pricelist_id.id != pricelist_id:
                        values['pricelist_id'] = pricelist_id
                        update_pricelist = True

                # if fiscal position, update the order lines taxes
                if sale_order.fiscal_position_id:
                    sale_order._compute_tax_id()

                # if values, then make the SO update
                if values:
                    sale_order.write(values)

                # check if the fiscal position has changed with the partner_id update
                recent_fiscal_position = sale_order.fiscal_position_id.id
                if flag_pricelist or recent_fiscal_position != fiscal_position:
                    update_pricelist = True
            if code2:
                sale_order._assign_voucher_code(code2)
                
            if code and code != sale_order.pricelist_id.code:
                code_pricelist = self.env['product.pricelist'].search([('code', '=', code)], limit=1)
                if code_pricelist:
                    pricelist_id = code_pricelist.id
                    update_pricelist = True
            elif code is not None and sale_order.pricelist_id.code:
                # code is not None when user removes code and click on "Apply"
                pricelist_id = partner.property_product_pricelist.id
                update_pricelist = True

            # update the pricelist
            if update_pricelist:
                request.session['website_sale_current_pl'] = pricelist_id
                values = {'pricelist_id': pricelist_id}
                sale_order.write(values)
                for line in sale_order.order_line:
                    if line.exists():
                        sale_order._cart_update(product_id=line.product_id.id, line_id=line.id, add_qty=0)

        else:
            request.session['sale_order_id'] = None
            return None

        return sale_order
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
