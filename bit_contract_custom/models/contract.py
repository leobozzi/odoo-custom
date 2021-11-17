# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class Contract(models.Model):
    _inherit = 'contract.contract'
    _description = "contract.contract"

    recurring_day = fields.Integer(
        string="Día del mes"
    )
    recurring_next_month = fields.Boolean(
        string="Próximo mes"
    )

    # Create Method
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            pass
        res = super(Contract, self).create(vals_list)
        return res

    # Write Method
    def write(self, vals):
        #raise ValidationError("Test: %s" % (vals))
        res = super(Contract, self).write(vals)
        return res
