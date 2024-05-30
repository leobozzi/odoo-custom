# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

import datetime


class UnbuildOrder(models.Model):
    _inherit = 'mrp.unbuild'
    _description = "mrp.unbuild"

    # Button Unbuild
    def action_validate(self):
        res = super(UnbuildOrder, self).action_validate()

        if self.mo_id.analytic_account_id:
            
            # MRP Cost
            vals_mrp_cost = {
                'date': datetime.date.today(),
                'name': self.name,
                'account_id': self.mo_id.analytic_account_id.id,
                'product_id': self.product_id.id,
                'unit_amount': self.product_qty,
                'product_uom_id': self.product_uom_id.id,
                'partner_id': '' if not self.mo_id.partner_id else self.mo_id.partner_id.id,
                'ref': '' if not self.mo_id.sale_id else self.mo_id.sale_id.name,
                'amount': self.product_qty * self.product_id.standard_price,
            }
            account_analytic_line_id = self.env['account.analytic.line'].create(vals_mrp_cost)

            # MRP Sale
            if self.mo_id.sale_id:
                order_line_ids = self.env['sale.order.line'].search([('order_id','=',self.mo_id.sale_id.id),('product_id','=',self.product_id.id)])
                order_line_price_unit = 0.0
                for order_line in order_line_ids:
                    order_line_price_unit = order_line.price_unit
                vals_mrp_sale = {
                    'date': datetime.date.today(),
                    'name': 'SALE-' + self.name,
                    'account_id': self.mo_id.analytic_account_id.id,
                    'product_id': self.product_id.id,
                    'unit_amount': self.product_qty,
                    'product_uom_id': self.product_uom_id.id,
                    'partner_id': '' if not self.mo_id.partner_id else self.mo_id.partner_id.id,
                    'ref': '' if not self.mo_id.sale_id else self.mo_id.sale_id.name,
                    'amount': -(self.product_qty * order_line_price_unit),
                }
                account_analytic_line_id = self.env['account.analytic.line'].create(vals_mrp_sale)
        return res



