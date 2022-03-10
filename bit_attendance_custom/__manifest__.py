# -*- coding: utf-8 -*-
{
    'name': "bit_attendance_custom",

    'summary': """
        Customización del módulo hr_attendance para el manejo de horas de empleados
    """,

    'description': """
        Customización del módulo de hr hr_attendance:
            - Se agregó el campo type_hour para diferenciar el tipo de hora.
            -
            -
    """,

    'author': "Leonardo Bozzi",
    'website': "https://www.vangrow.ar",

    # Categories can be used to filter modules in modules listing
    #
    # for the full list
    'category': 'attendance',
    'version': '0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': [
        'base', 'hr_attendance', 'project', 'bit_timesheet_custom',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/attendance_custom_data.xml',
        'view/hr_attendance_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
