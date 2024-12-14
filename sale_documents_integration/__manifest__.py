{
    "name": "Sale Documents Integration",
    "summary": "This module allows to save attachments of a sale order "
    "to a particular folder of Documents.",
    "version": "16.0.1.0.0",
    "category": "Documents",
    "author": "BizzAppDev Systems Pvt. Ltd.",
    "website": "http://www.bizzappdev.com",
    "license": "Other proprietary",
    "depends": [
        "sale_management",
        "documents",
    ],
    "data": [
        "data/document_data.xml",
        "views/res_config_settings_view.xml",
        "views/sale_order_views.xml",
    ],
    "images": ["images/sale_documents_integration.gif"],
    "installable": True,
    "auto_install": True,
}
