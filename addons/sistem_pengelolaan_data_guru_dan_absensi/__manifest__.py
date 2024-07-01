# -*- coding: utf-8 -*-
{
    'name': "Pengelolaan Data Guru & Absensi",

    'summary': """
        Sistem Pengelolaan Data Guru & Absensi Sekolah Dasar NEGERI SUMBERNONGKO""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/import_guru_wizard_views.xml',
        'views/data_guru_views.xml',
        'views/absensi_kehadiran_views.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
        'reports/report_data_guru.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
