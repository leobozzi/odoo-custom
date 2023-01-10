# -*- coding: utf-8 -*-
{
    'name': "bit_inmobiliaria_moreno",

    'summary': """
        Módulo que agrega cambios específicos para Inmobiliaria Gonzalo Moreno""",

    'description': """
        - Agrega mes de referencia a Factura de contrato.
    """,

    'author': "BozzIT",
    'website': "http://www.bozzit.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Ventas',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'contract'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/account_invoice_view.xml',
        'views/product_template_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
