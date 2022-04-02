# -*- coding: utf-8 -*-
{
    'name': "bit_mrp_sale_info_custom",

    'summary': """
        Customización del módulo mrp_sale_info para mostrar infoormación
        de la venta en la producción
    """,

    'description': """
        Customización del módulo de mrp_sale_inf:
            -
            -
            -
    """,

    'author': "Leonardo Bozzi",
    'website': "https://www.vangrow.ar",

    # Categories can be used to filter modules in modules listing
    #
    # for the full list
    'category': 'MRP',
    'version': '0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': [
        'base', 'mrp', 'sale',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/mrp_sale_info_custom_data.xml',
        'view/mrp_production_order_view.xml',
        'view/mrp_work_order_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
