# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


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
