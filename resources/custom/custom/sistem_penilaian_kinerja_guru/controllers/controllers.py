# -*- coding: utf-8 -*-
from odoo import http

# class SistemPenilaianKinerjaGuru(http.Controller):
#     @http.route('/sistem_penilaian_kinerja_guru/sistem_penilaian_kinerja_guru/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sistem_penilaian_kinerja_guru/sistem_penilaian_kinerja_guru/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sistem_penilaian_kinerja_guru.listing', {
#             'root': '/sistem_penilaian_kinerja_guru/sistem_penilaian_kinerja_guru',
#             'objects': http.request.env['sistem_penilaian_kinerja_guru.sistem_penilaian_kinerja_guru'].search([]),
#         })

#     @http.route('/sistem_penilaian_kinerja_guru/sistem_penilaian_kinerja_guru/objects/<model("sistem_penilaian_kinerja_guru.sistem_penilaian_kinerja_guru"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sistem_penilaian_kinerja_guru.object', {
#             'object': obj
#         })