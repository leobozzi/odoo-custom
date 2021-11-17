# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = "product.template"

    automatic_price = fields.Boolean(
        String="¿Precio Automático?"
    )
