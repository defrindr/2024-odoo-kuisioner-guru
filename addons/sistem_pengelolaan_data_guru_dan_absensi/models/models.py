# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sistem_pengelolaan_data_guru_dan_absensi(models.Model):
#     _name = 'sistem_pengelolaan_data_guru_dan_absensi.sistem_pengelolaan_data_guru_dan_absensi'
#     _description = 'sistem_pengelolaan_data_guru_dan_absensi.sistem_pengelolaan_data_guru_dan_absensi'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
