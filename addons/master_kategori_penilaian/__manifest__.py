# -*- coding: utf-8 -*-
{
    'name': "Master Kategori Penilaian",

    'summary': """
        Master Kategori Penilaian Sekolah Dasar NEGERI SUMBERNONGKO""",

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
        'seeder_data.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/kategori_jenis_views.xml',
        'views/kategori_group_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
