# -*- coding: utf-8 -*-
# from odoo import http


# class SistemPengelolaanDataGuruDanAbsensi(http.Controller):
#     @http.route('/sistem_pengelolaan_data_guru_dan_absensi/sistem_pengelolaan_data_guru_dan_absensi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sistem_pengelolaan_data_guru_dan_absensi/sistem_pengelolaan_data_guru_dan_absensi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sistem_pengelolaan_data_guru_dan_absensi.listing', {
#             'root': '/sistem_pengelolaan_data_guru_dan_absensi/sistem_pengelolaan_data_guru_dan_absensi',
#             'objects': http.request.env['sistem_pengelolaan_data_guru_dan_absensi.sistem_pengelolaan_data_guru_dan_absensi'].search([]),
#         })

#     @http.route('/sistem_pengelolaan_data_guru_dan_absensi/sistem_pengelolaan_data_guru_dan_absensi/objects/<model("sistem_pengelolaan_data_guru_dan_absensi.sistem_pengelolaan_data_guru_dan_absensi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sistem_pengelolaan_data_guru_dan_absensi.object', {
#             'object': obj
#         })
