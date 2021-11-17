# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class ContractTemplate(models.Model):
    _inherit = 'contract.template'
    _description = "contract.template"

    recurring_day = fields.Integer(
        string="Día del mes"
    )
    recurring_next_month = fields.Boolean(
        string="Próximo mes"
    )
