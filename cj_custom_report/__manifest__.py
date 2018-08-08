# -*- coding: utf-8 -*-
{
    'name': "cj_custom_report",

    'summary': """
        Custom Report Example""",

    'description': """
        Custom report for practice purpose
    """,

    'author': "Cak Juice",
    'website': "https://cakjuice.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_attendance'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'wizards/recap.xml',
        'reports/recap.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}