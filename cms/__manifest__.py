# -*- coding: utf-8 -*-
{
    'name': "CMS",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """Long description of module's purpose
    """,

    'author': "Iswe Solutions",
    'website': "https://www.Iswesolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project','approvals'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
        'installable': True,
        'auto_install': True,
        'application': True,
        'license': 'LGPL-3',
}

