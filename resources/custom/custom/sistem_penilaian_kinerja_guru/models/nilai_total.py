from odoo import _, api, fields, models
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT




class NilaiTotal(models.Model):
    _name = 'nilai.total'
    _description = 'Model untuk tabel data nilai total'

    name = fields.Date(string='Tanggal', default=datetime.now(), required=True)
    data_guru_id = fields.Many2one(comodel_name='data.guru', string='Nama Guru', required=True, ondelete="cascade")

    # HASIL PENILAIAN KEPALA SEKOLAH
    penilaian_kepala_sekolah = fields.Float(string='Hasil Penilaian Kepala Sekolah', compute="_compute_hasil_penilaian_kepala_sekolah")
    hasil_nilai_bobot_kepala_sekolah = fields.Float(string='Konversi Nilai (40%)', compute="_compute_hasil_nilai_bobot_kepala_sekolah")

    @api.depends('data_guru_id')
    def _compute_hasil_penilaian_kepala_sekolah(self):
        for rec in self:
            total_nilai=0
            menu1=self.env['penilaian.kepala.sekolah'].search([('data_guru_id.name','=',rec.data_guru_id.name)])
            if menu1:
                for a in menu1:
                    if rec.name.year == a.name.year:
                        total_nilai = sum([x.nilai_kinerja for x in menu1]) / sum([x.pembagi for x in menu1])
            rec.penilaian_kepala_sekolah = total_nilai

    @api.depends('penilaian_kepala_sekolah')
    def _compute_hasil_nilai_bobot_kepala_sekolah(self):
        for rec in self:
            rec.hasil_nilai_bobot_kepala_sekolah = rec.penilaian_kepala_sekolah * 40 / 100

    # HASIL PENILAIAN TEMAN SEJAWAT
    penilaian_teman_sejawat = fields.Float(string='Hasil Penilaian Teman Sejawat (Total Nilai Kinerja / Jumlah Responden)', compute="_compute_hasil_penilaian_teman_sejawat")
    hasil_nilai_bobot_teman_sejawat = fields.Float(string='Konversi Nilai (30%)', compute="_compute_hasil_nilai_bobot_teman_sejawat")
    
    @api.depends('data_guru_id')
    def _compute_hasil_penilaian_teman_sejawat(self):
        for rec in self:
            total_nilai=0
            menu2=self.env['penilaian.teman.sejawat'].search([('data_guru_id.name','=',rec.data_guru_id.name)])
            if menu2:
                for a in menu2:
                    if rec.name.year == a.name.year:
                        total_nilai = sum([x.nilai_kinerja for x in menu2]) / sum([x.pembagi for x in menu2])
            rec.penilaian_teman_sejawat = total_nilai

    @api.depends('penilaian_teman_sejawat')
    def _compute_hasil_nilai_bobot_teman_sejawat(self):
        for rec in self:
            rec.hasil_nilai_bobot_teman_sejawat = rec.penilaian_teman_sejawat * 30 / 100

    # HASIL PENILAIAN PESERTA DIDIK
    penilaian_peserta_didik = fields.Float(string='Hasil Penilaian Peserta Didik (Total Nilai Kinerja / Jumlah Responden)', compute="_compute_hasil_penilaian_peserta_didik")
    hasil_nilai_bobot_peserta_didik = fields.Float(string='Konversi Nilai (20%)', compute="_compute_hasil_nilai_bobot_peserta_didik")

    @api.depends('data_guru_id')
    def _compute_hasil_penilaian_peserta_didik(self):
        for rec in self:
            total_nilai=0
            menu3=self.env['penilaian.peserta.didik'].search([('data_guru_id.name','=',rec.data_guru_id.name)])
            if menu3:
                for a in menu3:
                    if rec.name.year == a.name.year:
                        total_nilai = sum([x.nilai_kinerja for x in menu3]) / sum([x.pembagi for x in menu3])
            rec.penilaian_peserta_didik = total_nilai

    @api.depends('penilaian_peserta_didik')
    def _compute_hasil_nilai_bobot_peserta_didik(self):
        for rec in self:
            rec.hasil_nilai_bobot_peserta_didik = rec.penilaian_peserta_didik * 20 / 100

    # HASIL PENILAIAN WALI MURIT
    penilaian_wali_murit = fields.Float(string='Hasil Penilaian Wali Murid (Total Nilai Kinerja / Jumlah Responden)', compute="_compute_hasil_penilaian_wali_murit")
    hasil_nilai_bobot_wali_murit = fields.Float(string='Konversi Nilai (10%)', compute="_compute_hasil_nilai_bobot_wali_murit")

    @api.depends('data_guru_id')
    def _compute_hasil_penilaian_wali_murit(self):
        for rec in self:
            total_nilai=0
            menu4=self.env['penilaian.wali.murit'].search([('data_guru_id.name','=',rec.data_guru_id.name)])
            if menu4:
                for a in menu4:
                    if rec.name.year == a.name.year:
                        total_nilai = sum([x.nilai_kinerja for x in menu4]) / sum([x.pembagi for x in menu4])
            rec.penilaian_wali_murit = total_nilai

    @api.depends('penilaian_wali_murit')
    def _compute_hasil_nilai_bobot_wali_murit(self):
        for rec in self:
            rec.hasil_nilai_bobot_wali_murit = rec.penilaian_wali_murit * 10 / 100    

    # TOTAL NILAI
    total_nilai = fields.Float(string='Total Nilai', compute="_compute_total_nilai", store=True)

    @api.depends('name','hasil_nilai_bobot_kepala_sekolah','hasil_nilai_bobot_teman_sejawat','hasil_nilai_bobot_peserta_didik','hasil_nilai_bobot_wali_murit')
    def _compute_total_nilai(self):
        for rec in self:
            rec.total_nilai = rec.hasil_nilai_bobot_kepala_sekolah + rec.hasil_nilai_bobot_teman_sejawat + rec.hasil_nilai_bobot_peserta_didik + rec.hasil_nilai_bobot_wali_murit

    


            
    