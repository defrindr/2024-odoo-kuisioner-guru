# -*- coding: utf-8 -*-
{
    'name': "Sistem Penilaian Baru",

    'summary': """
        Sistem Penilaian Baru di Sekolah Dasar NEGERI SUMBERNONGKO""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    'qweb': [
        '/static/src/xml/console_log_widget_template.xml',
    ],
    # always loaded
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml', 
        "views/assets.xml",
        "views/tes.xml",
        "views/total_nilai.xml",
        "views/graph_total_nilai.xml",
        'reports/report_total_nilai.xml',
        "views/mpenilaian_kepsek_views.xml",
    ],
    "application": True,
    "installable": True
}