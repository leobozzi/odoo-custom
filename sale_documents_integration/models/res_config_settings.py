from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    # Added new fields for sale order config. #T6320
    documents_sale_order_settings = fields.Boolean(
        related="company_id.documents_sale_order_settings",
        readonly=False,
        string="Sale Order",
    )
    sale_order_folder_id = fields.Many2one(
        comodel_name="documents.folder",
        related="company_id.sale_order_folder_id",
        readonly=False,
        string="Sale Order Default Workspace",
    )
