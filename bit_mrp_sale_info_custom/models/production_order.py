# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

import datetime


class ProductionOrder(models.Model):
    _inherit = 'mrp.production'
    _description = "mrp.production"

    sale_id = fields.Many2one(
        comodel_name='sale.order',
        string="Sale order",
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Customer",
        related='sale_id.partner_id',
        readonly=True,
        store=True
    )
    tag_ids = fields.Many2many(
        comodel_name='mrp.production.tag',
        string="Tags"
    )

    @api.onchange('sale_id')
    def _onchange_sale_id(self):
        self.analytic_account_id = self.sale_id.analytic_account_id

    # Button Mark Done
    def button_mark_done(self):
        res = super(ProductionOrder, self).button_mark_done()

        if self.analytic_account_id:
            vals = {
                'date': datetime.date.today(),
                'name': self.name,
                'account_id': self.analytic_account_id.id,
                'product_id': self.product_id.id,
                'unit_amount': self.product_qty,
                'product_uom_id': self.product_uom_id.id,
                'partner_id': '' if not self.partner_id else self.partner_id.id,
                'ref': '' if not self.sale_id else self.sale_id.name,
                'amount': -(self.product_qty * self.product_id.standard_price),
            }
            account_analytic_line_id = self.env['account.analytic.line'].create(vals)
        return res
