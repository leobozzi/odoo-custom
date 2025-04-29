# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Website Denomination Gift Voucher',
    'category': 'Website',
    'summary': 'Website Denomination Gift Voucher Discount',
    'version': '15.0.0.0',
    'description': """
		This module helps to generate website gift voucher denomination,Website Discount voucher, Website Promocode, Website Denomination Discount, website Gift denomination voucher
=======        """,
    'author': 'Browseinfo',
    'website': 'https://www.browseinfo.com',
    'depends': ['base','account', 'sale','product','website_sale','sale_management'],
    'data': [
            'security/ir.model.access.csv',
            'views/views.xml',
            'views/templates.xml',
            'views/denomination_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'OPL-1',
    'live_test_url':'https://youtu.be/nu8VxRXJVHw',
    "images":['static/description/Banner.png'],
}
