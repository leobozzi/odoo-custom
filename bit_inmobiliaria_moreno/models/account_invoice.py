# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    _description = 'account.invoice'

    month = fields.Char(
        string="Mes",
        compute='_compute_month',
    )

    @api.depends('date_invoice')
    def _compute_month(self):
        month_list = ['', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        for res in self:
            try:
                res.month = month_list[res.date_invoice.month]
            except:
                pass
