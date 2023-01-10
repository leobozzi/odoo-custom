# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class AnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'
    _description = 'account.analytic.account'

    is_property = fields.Boolean(
        string="Es propietario"
    )

    date = fields.Date(
        string = "Fecha",
    )

    description = fields.Html(
        string="Encabezado",
    )


