# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

import datetime
import dateutil


class ContractLine(models.Model):
    _inherit = 'contract.line'
    _description = "contract.line"

    # Create Method
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            product_id = self.env['product.product'].browse(vals['product_id'])
            if product_id.automatic_price:
                vals['automatic_price'] = True
                if product_id.property_contract_template_id.recurring_day != 0:
                    recurring_next_date = datetime.datetime.now().replace(day=product_id.property_contract_template_id.recurring_day) if not product_id.property_contract_template_id.recurring_next_month else datetime.datetime.now(
                    ).replace(day=product_id.property_contract_template_id.recurring_day) + dateutil.relativedelta.relativedelta(months=1)
                vals['recurring_next_date'] = recurring_next_date.date()
        res = super(ContractLine, self).create(
            vals_list)
        return res

        # Write Method
        def write(self, vals):
            # raise ValidationError("Test: %s" % (vals))
            res = super(ContractLine, self).write(vals)
            return res
