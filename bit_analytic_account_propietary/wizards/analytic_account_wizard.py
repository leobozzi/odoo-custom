# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

import datetime

class AnalyticAccountWizard(models.TransientModel):
    _name = 'analytic.account.wizard'
    _description = 'analytic.account.wizard'

    date = fields.Date(
        string="Fecha",
    )
