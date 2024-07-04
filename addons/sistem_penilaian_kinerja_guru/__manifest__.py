# -*- coding: utf-8 -*-
{
    'name': "Sistem Penilaian Kinerja Guru",

    'summary': """
        Sistem Penilaian Kinerja Guru di Sekolah Dasar NEGERI SUMBERNONGKO""",

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
    'depends': ['base'],

    # always loaded
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',  # Path ke file ir_rule.xml
        'views/nilai_total.xml',
        'reports/report_total_nilai.xml',
        'views/templates.xml',
        'views/penilaian_kepala_sekolah.xml',
        'views/penilaian_teman_sejawat.xml',
        'views/penilaian_wali_murit.xml',
        'views/penilaian_peserta_didik.xml',
        'views/views.xml',
        'views/graph_total_nilai.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}