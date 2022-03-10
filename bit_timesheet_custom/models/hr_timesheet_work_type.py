# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class TimesheetWorkType(models.Model):
    _name = 'account.analytic.line.worktype'
    _description = "account.analytic.line.worktype"

    name = fields.Char(
        string="Description",
    )

    type = fields.Char(
        string="Type"
    )
