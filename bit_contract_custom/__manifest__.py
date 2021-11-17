# -*- coding: utf-8 -*-
{
    'name': "bit_contract_custom",

    'summary': """
        Customización del módulo de contrato adaptado a empresas de servicio de telecomunicaciones
    """,

    'description': """
        Customización del módulo de contrato telecomunicaciones:
            - Se agregó el campo automatic_price en el template del producto de contrato.
            -
            -
    """,

    'author': "Leonardo Bozzi",
    'website': "https://www.vangrow.ar",

    # Categories can be used to filter modules in modules listing
    #
    # for the full list
    'category': 'Contract',
    'version': '0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': [
        'base', 'sale', 'contract', 'contract_sale', 'product_contract',
        ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'view/product_template_view.xml',
        'view/contract_template_view.xml',
        ],

    'installable': True,
    'auto_install': False,
    'application': False,

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
