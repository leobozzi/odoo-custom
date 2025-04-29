# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

import werkzeug
import odoo
from odoo import addons
from odoo import models, fields, api
from odoo import SUPERUSER_ID
from odoo import http, tools, _
from odoo.http import request
from odoo.tools.translate import _
import odoo.http as http
from odoo.http import request

import werkzeug.urls
import werkzeug.wrappers
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.payment.controllers.post_processing import PaymentPostProcessing

class voucher_discount(http.Controller):

    @http.route(['/shop/voucher'], type='http', auth="public", website=True)
    def voucher_code(self, promo, **post):
        
        dv = request.env['gift.voucher'].search([('name', '=', promo)])
        if not dv:
            return request.redirect("/shop/cart?gift_msg=%s" % _("Invalid Voucher !"))
        else:
            dv = request.env['gift.voucher'].browse(dv).id
            if dv.used == True:
                return request.redirect("/shop/cart?gift_msg=%s" % _("This code has been already used !"))

            request.website.sale_get_order(code2=promo)
            return request.redirect("/shop/cart")
            

class website_sale_inherit(WebsiteSale):

    @http.route('/shop/payment/validate', type='http', auth="public", website=True)
    def payment_validate(self, transaction_id=None, sale_order_id=None, **post):
        """ Method that should be called by the server when receiving an update
        for a transaction. State at this point :

         - UDPATE ME
        """
        if sale_order_id is None:
            order = request.website.sale_get_order()
        else:
            order = request.env['sale.order'].sudo().browse(sale_order_id)
            assert order.id == request.session.get('sale_last_order_id')

        if transaction_id:
            tx = request.env['payment.transaction'].sudo().browse(transaction_id)
            assert tx in order.transaction_ids()
        elif order:
            tx = order.get_portal_last_transaction()
        else:
            tx = None

        if not order or (order.amount_total and not tx):
            return request.redirect('/shop')



#
        if order.voucher_code:
            voucher_id = request.env['gift.voucher'].search([('name', '=', order.voucher_code)])
            
            voucher_id.write({'used':True})
#
                    
                    
        if (not order.amount_total and not tx) or tx.state in ['pending', 'done', 'authorized']:
            if (not order.amount_total and not tx):
                # Orders are confirmed by payment transactions, but there is none for free orders,
                # (e.g. free events), so confirm immediately
                order.with_context(send_email=True).action_confirm()
        elif tx and tx.state == 'cancel':
            # cancel the quotation
            order.action_cancel()

        # clean context and session, then redirect to the confirmation page
        request.website.sale_reset()
        if tx and tx.state == 'draft':
            return request.redirect('/shop')

        PaymentPostProcessing.remove_transactions(tx)
        return request.redirect('/shop/confirmation')
       

class denomination_voucher(http.Controller):

    # Add Message in Cart page...        
    @http.route(['/shop/addmessage'], type='http', auth="public", methods=['POST'], website=True)
    def add_message(self, **post):
        
        orm_partner = request.env['res.partner']
        
        order = request.website.sale_get_order(force_create=1)
        
        message = post['message']

        vals = {'message':message}

        sale_order_obj = order.write(vals)
        
        return request.redirect("/shop/cart")

