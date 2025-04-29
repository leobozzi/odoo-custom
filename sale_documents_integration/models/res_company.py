from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    def _domain_company(self):
        """Added new method for return domain. #T6320"""
        company = self.env.company
        return ["|", ("company_id", "=", False), ("company_id", "=", company.id)]

    # Added fields for sale order configuration. #T6320
    documents_sale_order_settings = fields.Boolean(default=True)
    sale_order_folder_id = fields.Many2one(
        comodel_name="documents.folder",
        string="Sale Order Workspace",
        domain=_domain_company,
        default=lambda self: self.env.ref(
            "sale_documents_integration.sale_documents_integration_sale_documents_folder",  # noqa: B950
            raise_if_not_found=False,
        ),
    )
