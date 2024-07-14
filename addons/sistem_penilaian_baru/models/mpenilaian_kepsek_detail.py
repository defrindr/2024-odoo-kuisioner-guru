from odoo import models,fields,api
from datetime import date, datetime

class MpenilaianKepsek(models.Model):
    _name="mpenilaian.kepsek.detail"
    _description="Model untuk Detail Penialaian Kepsek"
    
    penilaian_id = fields.Many2one(comodel_name='mpenilaian.kepsek', string='Penilaian', required="True", ondelete="cascade")
    jenis_id = fields.Many2one(comodel_name='kategori.jenis', string='Penilaian', required="True", ondelete="cascade")
    keterangan_id = fields.Many2one(comodel_name='kategori.keterangan', string='Item Penilaian', required="True", ondelete="cascade")
    nilai = fields.Selection(string='Nilai', selection=[('sering', 'Sering'), ('kadang_kadang', 'Kadang-kadang'),('tidak_pernah','Tidak Pernah')])

    def get_grouped_data(self):
        records = self.search([])
        grouped_data = {}
        for record in records:
            group = record.jenis_id
            if group not in grouped_data:
                grouped_data[group] = []
            grouped_data[group].append(record)
        return grouped_data
