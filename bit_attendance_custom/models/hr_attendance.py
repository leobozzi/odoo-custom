# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

import datetime


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'
    _description = "hr.attendance"

    # Set default worktype
    @api.model
    def _default_work_type(self):
        worktype_id = self.env['account.analytic.line.worktype'].search([])
        if worktype_id:
            return worktype_id[0]
        return None

    worktype_id = fields.Many2one(
        comodel_name='account.analytic.line.worktype',
        string="Type",
        required=True,
        default=_default_work_type
    )
    project_id = fields.Many2one(
        comodel_name="project.project",
        string="Project",
    )
    task_id = fields.Many2one(
        comodel_name="project.task",
        string="Task",
    )
    account_analytic_line_id = fields.Many2one(
        comodel_name='account.analytic.line',
        string="Timesheet",
    )

    @api.onchange('project_id')
    def onchange_project_id(self):
        self.task_id = False
        res = {'domain': {
            'task_id': [('project_id', '=', self.project_id.id)],
        }}
        return res

    # Create Method
    @api.model
    def create(self, vals):
        res = super(HrAttendance, self).create(vals)
        date = False
        start_time = False
        stop_time = False
        hours = 0.0
        if 'check_in' in vals:
            date = datetime.datetime.strptime(
                vals['check_in'], '%Y-%m-%d %H:%M:%S').date() if isinstance(vals['check_in'], str) else vals['check_in'].date()
            start_time = datetime.datetime.strptime(
                vals['check_in'], '%Y-%m-%d %H:%M:%S') if isinstance(vals['check_in'], str) else vals['check_in']
        if 'check_out' in vals:
            stop_time = datetime.datetime.strptime(
                vals['check_out'], '%Y-%m-%d %H:%M:%S') if isinstance(vals['check_out'], str) else vals['check_out']
            hours = (stop_time - start_time).total_seconds() / 3600.0
        project_id = False if 'project_id' not in vals else self.env['project.project'].search(
            [('id', '=', vals['project_id'])])
        task_id = False if 'task_id' not in vals else self.env['project.task'].search(
            [('id', '=', vals['task_id'])])
        description = '' if project_id.name is False else project_id.name
        description = description if task_id.name is False else description + ' - ' + task_id.name
        info = {
            'date': date,
            'employee_id': vals['employee_id'],
            'name': description,
            'project_id': project_id.id,
            'task_id': task_id.id,
            'worktype_id': False if 'worktype_id' not in vals else vals['worktype_id'],
            'unit_amount': hours,
        }
        if info['project_id']:
            account_analytic_line_id = self.env['account.analytic.line'].create(
                info)
            res.account_analytic_line_id = account_analytic_line_id
        return res

    # Write Method
    def write(self, vals):
        res = super(HrAttendance, self).write(vals)
        date = self.check_in.date()
        hours = (self.check_out - self.check_in).total_seconds() / 3600.0
        project_id = self.env['project.project'].search(
            [('id', '=', self.project_id.id)])
        task_id = self.env['project.task'].search(
            [('id', '=', self.task_id.id)])
        description = '' if project_id.name is False else project_id.name
        description = description if task_id.name is False else description + ' - ' + task_id.name
        info = {
            'date': date,
            'employee_id': self.employee_id.id,
            'name': description,
            'project_id': project_id.id,
            'task_id': task_id.id,
            'worktype_id': self.worktype_id.id,
            'unit_amount': hours,
        }

        if info['project_id']:
            if self.account_analytic_line_id:
                self.account_analytic_line_id.write(info)
            else:
                account_analytic_line_id = self.env['account.analytic.line'].create(
                    info)
                self.account_analytic_line_id = account_analytic_line_id
        else:
            if self.account_analytic_line_id:
                self.account_analytic_line_id.unlink()
        return res

    # Unlink Method
    def unlink(self):
        if self.account_analytic_line_id:
            self.account_analytic_line_id.unlink()

        res = super(HrAttendance, self).unlink()
        return res
