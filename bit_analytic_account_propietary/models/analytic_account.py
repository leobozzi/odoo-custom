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

    dynamic_description = fields.Text(
        string="Dynamic Description",
    )

    @api.onchange('description')
    def _onchange_description(self):
        description = ''
        #DIA#
        description = self.description.replace("#DIA#", str(self.date.day))
        #MES#
        if self.date.month == 1:
            description = description.replace("#MES#", "ENERO")
        elif analytic.date.month == 2:
            description = description.replace("#MES#", "FEBRERO")
        elif analytic.date.month == 2:
            description = description.replace("#MES#", "MARZO")
        elif analytic.date.month == 2:
            description = description.replace("#MES#", "ABRIL")
        elif analytic.date.month == 2:
            description = description.replace("#MES#", "MAYO")
        elif analytic.date.month == 2:
            description = description.replace("#MES#", "JUNIO")
        elif analytic.date.month == 2:
            description = description.replace("#MES#", "JULIO")
        elif analytic.date.month == 2:
            description = description.replace("#MES#", "AGOSTO")
        elif analytic.date.month == 2:
            description = description.replace("#MES#", "SEPTIEMBRE")
        elif analytic.date.month == 2:
            description = description.replace("#MES#", "OCTUBRE")
        elif analytic.date.month == 2:
            description = description.replace("#MES#", "NOVIEMBRE")
        elif analytic.date.month == 2:
            description = description.replace("#MES#", "DICIEMBRE")
        #AÑO#
        description = description.replace("#AÑO#", str(self.date.year))
        
        self.dynamic_description = description
