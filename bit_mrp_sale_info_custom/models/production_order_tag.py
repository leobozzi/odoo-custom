# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

import random


class WorkOrderTag(models.Model):
    _name = 'mrp.production.tag'
    _description = "mrp.production.tag"

    def _get_default_color(self):
        return random.randint(1, 11)

    name = fields.Char(
        string="Tags",
        required=True
    )

    color = fields.Integer(
        string="Color Index",
        default=_get_default_color
    )
