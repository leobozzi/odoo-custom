# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class TimesheetLine(models.Model):
    _inherit = 'account.analytic.line'
    _description = "account.analytic.line"

    worktype_id = fields.Many2one(
        comodel_name='account.analytic.line.worktype',
        string="Tipo",
    )

    @api.onchange('project_id')
    def _onchange_project_id(self):
        if self.name is False and self.project_id and self.worktype_id:
            self.name = self.project_id.name + '-' + self.worktype_id.name

    @api.onchange('worktype_id')
    def _onchange_worktype_id(self):
        if self.name is False and self.project_id and self.worktype_id:
            self.name = self.project_id.name + '-' + self.worktype_id.name
