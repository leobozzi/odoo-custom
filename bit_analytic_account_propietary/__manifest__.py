# -*- coding: utf-8 -*-
{
    'name': "bit_analytic_account_propietary",

    'summary': """
        Módulo que agrega un reporta a las cuentas analìticas de los propietarios""",

    'description': """
        - Genera un reporte de los movimientos en fechas especìficas.
    """,

    'author': "BozzIT",
    'website': "http://www.bozzit.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Ventas',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'analytic'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/analytic_account_view.xml',
        'views/analytic_account_propietary_report.xml',
        #'data/analytic_account_data.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
