from odoo import fields, models


class Document(models.Model):
    _inherit = "documents.document"

    # Added new fields. #T6320
    sale_id = fields.Many2one(
        comodel_name="sale.order", string="Sale Order", copy=False, ondelete="restrict"
    )
    folder_id = fields.Many2one(
        comodel_name="documents.folder",
        string="Workspace",
        ondelete="restrict",
        tracking=True,
        required=True,
        index=True,
    )
