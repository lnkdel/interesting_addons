# -*- coding: utf-8 -*-
{
    'name': "api_v1",

    'summary': """
        Odoo Web Api V1""",

    'description': """
        Odoo Web Api V1
    """,

    'author': "HSIT",
    'website': "http://www.hscarbonfibre.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'api_base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}