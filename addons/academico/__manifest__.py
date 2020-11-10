# -*- coding: utf-8 -*-
{
    'name': "academico",

    'summary': """
       Treinamento de ODOO""",

    'description': """
        Treinamento de ODOO. Construindo um módulo do zero
    """,

    'author': "MyIA",
    'website': "http://www.myia.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/academico.xml',
        'views/partner.xml',
        'report.xml',
        'views/session_board.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
