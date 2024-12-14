from odoo.tests import TransactionCase


class TestSaleOrderDocuments(TransactionCase):
    def setUp(self):
        """Inherit the method to set up initial data for test cases.#T6320"""
        super().setUp()
        # Retrieve sale order record.#T6320
        self.sale_order = self.env.ref("sale.sale_order_7")
        # Retrieve document folder record.#T6320
        self.document_folder = self.env.ref(
            "sale_documents_integration.sale_documents_integration_sale_documents_folder"  # noqa:B950
        )
        # Create documents related to the sale order.#T6320
        self.doc1 = self.env["documents.document"].create(
            {
                "name": "Test Document 1",
                "sale_id": self.sale_order.id,
                "folder_id": self.document_folder.id,
            }
        )
        self.doc2 = self.env["documents.document"].create(
            {
                "name": "Test Document 2",
                "sale_id": self.sale_order.id,
                "folder_id": self.document_folder.id,
            }
        )

    def test_sale_document_count(self):
        """New Test method to ensure the sale document count functionality.#T6320"""
        # Ensure sale_document_count is computed correctly.#T6320
        self.assertEqual(
            self.sale_order.sale_document_count,
            2,
            "Sale document count does not match expected value.",
        )

    def test_action_sale_open_documents(self):
        """New Test method to ensure the action for opening sale documents
        functionality #T6320"""
        # Call action to open sale documents.#T6320
        action_window = self.sale_order.action_sale_open_documents()
        # Assert that the res_model of action window is correct
        self.assertEqual(
            action_window["res_model"],
            "documents.document",
            "Incorrect res_model in action window.",
        )
        # Assert that the domain of action window is correct.#T6320
        self.assertEqual(
            action_window["domain"],
            [("sale_id", "=", self.sale_order.id)],
            "Incorrect domain in action window.",
        )
        # Assert that the default_sale_id of action window is correct.#T6320
        self.assertEqual(
            action_window["context"]["default_sale_id"],
            self.sale_order.id,
            "Incorrect default_sale_id in context of action.",
        )
