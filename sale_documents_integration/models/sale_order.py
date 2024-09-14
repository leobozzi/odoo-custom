from odoo import _, fields, models


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = ["sale.order", "documents.mixin"]

    sale_document_count = fields.Integer(compute="_compute_sale_document_count")

    def _get_document_folder(self):
        """Added method for return document folder. #T6320"""
        if not self.company_id.documents_sale_order_settings:
            return False
        return self.company_id.sale_order_folder_id

    def _get_document_vals(self, attachment):
        """Inherit method to pass the sale_id for documents #T6320"""
        document_vals = super()._get_document_vals(attachment)
        # update documents_vals dict with sale_id #T6320
        document_vals.update({"sale_id": self.id})
        return document_vals

    def _compute_sale_document_count(self):
        """New Method for count documents of sale order. #T6320"""
        for order in self:
            documents = self.env["documents.document"].search_count(
                [("sale_id", "=", order.id)]
            )
            order.sale_document_count = documents

    def action_sale_open_documents(self):
        """New method for open documents kanban view. #T6320"""
        self.ensure_one()
        sale_folder = self._get_document_folder()
        action_window = {
            "type": "ir.actions.act_window",
            "res_model": "documents.document",
            "name": _("Documents"),
            "view": [[False, "kanban"], [False, "tree"]],
            "view_mode": "kanban,tree",
            "domain": [("sale_id", "=", self.id)],
            "context": {
                "default_sale_id": self.id,
                "searchpanel_default_folder_id": sale_folder and sale_folder.id,
                "custom_sale_model": True,
            },
        }
        return action_window
