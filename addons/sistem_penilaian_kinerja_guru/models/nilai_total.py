import locale
from odoo import _, api, fields, models
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT



import logging
_logger = logging.getLogger(__name__)

class NilaiTotal(models.Model):
    _name = 'nilai.total'
    _description = 'Model untuk tabel data nilai total'

    name = fields.Date(string='Tanggal', default=datetime.now(), required=True)
    @api.depends('name')
    def _compute_tanggal_indonesia(self):
        for order in self:
            if order.name:
                tanggal = order.name.strftime('%d %B %Y')
                order.tanggal_indonesia = self._map_format_tanggal(tanggal)

    def _map_format_tanggal(self, tanggal):
        format_mapping = {
            '01': '01', '02': '02', '03': '03', '04': '04', '05': '05', '06': '06',
            '07': '07', '08': '08', '09': '09', '10': '10', '11': '11', '12': '12',
            'January': 'Januari', 'February': 'Februari', 'March': 'Maret',
            'April': 'April', 'May': 'Mei', 'June': 'Juni', 'July': 'Juli',
            'August': 'Agustus', 'September': 'September', 'October': 'Oktober',
            'November': 'November', 'December': 'Desember'
        }

        parts = tanggal.split()
        day = parts[0]
        month = format_mapping[parts[1]]
        year = parts[2]

        return f"{day} {month} {year}"

    tanggal_indonesia = fields.Char(string="Tanggal (Indonesia)", compute='_compute_tanggal_indonesia', store=True)

    data_guru_id = fields.Many2one(comodel_name='data.guru', string='Nama Guru', required=True, ondelete="cascade")

    data_kepala_sekolah_id = fields.Many2one(comodel_name='res.users', string='Nama Kepala Sekolah', ondelete="cascade", compute="_compute_kepala_sekolah", store=True)
    
    @api.depends('data_guru_id')
    def _compute_kepala_sekolah(self):
        for rec in self:
            # Retrieve users belonging to a specific group ID
            group = self.env['res.groups'].browse(24)
            rec.data_kepala_sekolah_id=1
            print(group)
            if group:
                users = group.users
                if users:
                    rec.data_kepala_sekolah_id = users[0].id
                    _logger.info('pon', users[0].id)
                else:
                    _logger.info('notpon')
                    rec.data_kepala_sekolah_id = -1
            else:
                rec.data_kepala_sekolah_id = 0
                _logger.info('notpon')

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

    


            
    