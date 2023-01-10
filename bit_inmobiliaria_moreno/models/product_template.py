# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class ProductTemplateInmobiliaria(models.Model):
    _inherit = 'product.template'
    _description = 'product.template'

    product_services_ids = fields.One2many(
        comodel_name="product.services",
        inverse_name="parent_id"
    )


class Productservices(models.Model):
    _name = 'product.services'
    _description = 'product.services'

    parent_id = fields.Many2one(
        comodel_name="product.template",
        string="Parent"
    )
    product_id = fields.Many2one(
        comodel_name="product.template",
        string="Servicio"
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Socio",
    )
    partner_number = fields.Char(
        string="Número de Socio"
    )
    account_number = fields.Char(
        string="Numero de Cuenta"
    )
