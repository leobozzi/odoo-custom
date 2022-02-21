# -*- coding: utf-8 -*-
{
    'name': "bit_timesheet_custom",

    'summary': """
        Customización del módulo hr_timesheet para el manejo de horas de empleados
    """,

    'description': """
        Customización del módulo de hr hr_timesheet:
            - Se agregó el campo type_work para diferenciar el tipo de hora.
            -
            -
    """,

    'author': "Leonardo Bozzi",
    'website': "https://www.vangrow.ar",

    # Categories can be used to filter modules in modules listing
    #
    # for the full list
    'category': 'Timesheet',
    'version': '0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': [
        'base', 'hr_timesheet',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/timesheet_custom_data.xml',
        'view/hr_timesheet_line_view.xml',
        'view/hr_timesheet_work_type_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
