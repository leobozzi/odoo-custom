# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class WorkOrder(models.Model):
    _inherit = 'mrp.workorder'
    _description = "mrp.workorder"

    sale_id = fields.Many2one(
        related="production_id.sale_id",
        string="Sale order",
        readonly=True,
        store=True
    )
    partner_id = fields.Many2one(
        related="sale_id.partner_id",
        readonly=True,
        string="Customer",
        store=True
    )
    code = fields.Char(
        related="workcenter_id.code",
        readonly=True,
        string="Code",
        store=True
    )
