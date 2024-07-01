from odoo import _, api, fields, models
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT




class PenilaianWaliMurit(models.Model):
    _name = 'penilaian.wali.murit'
    _description = 'Model untuk tabel data penilaian guru oleh wali murit'

    name = fields.Date(string='Tanggal Penilaian', default=datetime.now(), required=True)
    nama_responden = fields.Char(string='Nama Responden', required=True)
    jabatan = fields.Char(string='Jabatan', default='Wali Murid/Orang Tua', readonly=True)
    data_guru_id = fields.Many2one(comodel_name='data.guru', string='Guru yang di nilai', required=True, ondelete="cascade")

    # ini kuisioner di dalam notebook :
    #1. Komunikasi
    a = fields.Selection(string="Guru memberitahukan perkembangan belajar putra/putri saya..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    b = fields.Selection(string="Guru  memberi kesempatan berkomunikasi dengan saya yang berkaitan dengan perilaku atau kesulitan belajar..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    c = fields.Selection(string="Guru bekerja sama dengan orang tua untuk menyelesaikan kesulitan belajar putra/putri saya..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])

    # Nilai per kategory
    nilai_a = fields.Integer(string='',compute="compute_nilai_a")
    @api.depends('a')
    def compute_nilai_a(self):
        for rec in self:
            if rec.a == 'sering':
                rec.nilai_a = 2
            elif rec.a == 'kadang-kadang':
                rec.nilai_a = 1
            else:
                rec.nilai_a = 0
    
    nilai_b = fields.Integer(string='',compute="compute_nilai_b")
    @api.depends('b')
    def compute_nilai_b(self):
        for rec in self:
            if rec.b == 'sering':
                rec.nilai_b = 2
            elif rec.b == 'kadang-kadang':
                rec.nilai_b = 1
            else:
                rec.nilai_b = 0
    nilai_c = fields.Integer(string='',compute="compute_nilai_c")
    @api.depends('c')
    def compute_nilai_c(self):
        for rec in self:
            if rec.c == 'sering':
                rec.nilai_c = 2
            elif rec.c == 'kadang-kadang':
                rec.nilai_c = 1
            else:
                rec.nilai_c = 0

    nilai_total_komunikasi = fields.Float(string='Nilai Total', compute='compute_nilai_total_komunikasi')
    @api.depends('nilai_a','nilai_b','nilai_c')
    def compute_nilai_total_komunikasi(self):
        for rec in self:
            rec.nilai_total_komunikasi = rec.nilai_a + rec.nilai_b + rec.nilai_c 

    #2. Kepercayaan dalam memberikan pendidikan kepada peserta didik
    a1 = fields.Selection(string="Guru berperan sebagai orang tua bagi putra/putri saya di sekolah..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    b1 = fields.Selection(string="Guru mengubah perilaku putra/putri saya menjadi lebih baik..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    c1 = fields.Selection(string="Guru memberikan bimbingan dalam pembelajaran kepada putra/putri saya yang dapat dimanfaatkan dalam kehidupan sehari-hari..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    d1 = fields.Selection(string="Guru disenangi oleh putra/putri saya dan teman-temannya..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    e1 = fields.Selection(string="Guru mengembalikan hasil belajar (PR, tugas, hasil ulangan) putra/putri saya dilengkapi dengan catatan..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])

    # Nilai per kategory
    nilai_a1 = fields.Integer(string='',compute="compute_nilai_a1")
    @api.depends('a1')
    def compute_nilai_a1(self):
        for rec in self:
            if rec.a1 == 'sering':
                rec.nilai_a1 = 2
            elif rec.a1 == 'kadang-kadang':
                rec.nilai_a1 = 1
            else:
                rec.nilai_a1 = 0
    
    nilai_b1 = fields.Integer(string='',compute="compute_nilai_b1")
    @api.depends('b1')
    def compute_nilai_b1(self):
        for rec in self:
            if rec.b1 == 'sering':
                rec.nilai_b1 = 2
            elif rec.b1 == 'kadang-kadang':
                rec.nilai_b1 = 1
            else:
                rec.nilai_b1 = 0
    nilai_c1 = fields.Integer(string='',compute="compute_nilai_c1")
    @api.depends('c1')
    def compute_nilai_c1(self):
        for rec in self:
            if rec.c1 == 'sering':
                rec.nilai_c1 = 2
            elif rec.c1 == 'kadang-kadang':
                rec.nilai_c1 = 1
            else:
                rec.nilai_c1 = 0
    nilai_d1 = fields.Integer(string='',compute="compute_nilai_d1")
    @api.depends('d1')
    def compute_nilai_d1(self):
        for rec in self:
            if rec.d1 == 'sering':
                rec.nilai_d1 = 2
            elif rec.d1 == 'kadang-kadang':
                rec.nilai_d1 = 1
            else:
                rec.nilai_d1 = 0
    nilai_e1 = fields.Integer(string='',compute="compute_nilai_e1")
    @api.depends('e1')
    def compute_nilai_e1(self):
        for rec in self:
            if rec.e1 == 'sering':
                rec.nilai_e1 = 2
            elif rec.e1 == 'kadang-kadang':
                rec.nilai_e1 = 1
            else:
                rec.nilai_e1 = 0
                
    nilai_total_kepercayaan_dalam_memberikan_pendidikan_kepada_peserta_didik = fields.Float(string='Nilai Total', compute='compute_nilai_total_kepercayaan_dalam_memberikan_pendidikan_kepada_peserta_didik')
    @api.depends('nilai_a1','nilai_b1','nilai_c1','nilai_d1','nilai_e1')
    def compute_nilai_total_kepercayaan_dalam_memberikan_pendidikan_kepada_peserta_didik(self):
        for rec in self:
            rec.nilai_total_kepercayaan_dalam_memberikan_pendidikan_kepada_peserta_didik = rec.nilai_a1 + rec.nilai_b1 + rec.nilai_c1 + rec.nilai_d1 + rec.nilai_e1
    
    # PERHITUNGAN NILAI KINERJA
    jumlah_indikator = fields.Float(string='Jumlah Indikator', readonly=True, default=8)
    skor_maksimum = fields.Float(string='Skor Maksimum', compute="_compute_skor_maksimum")
    jumlah_skor = fields.Float(string='Jumlah Skor', compute="_compute_jumlah_skor")
    nilai_kinerja = fields.Float(string='Nilai Kinerja', compute="_compute_nilai_kinerja")
    
    
    @api.depends('jumlah_indikator')
    def _compute_skor_maksimum(self):
        for rec in self:
            rec.skor_maksimum = rec.jumlah_indikator * 2

    
    @api.depends('nilai_total_komunikasi','nilai_total_kepercayaan_dalam_memberikan_pendidikan_kepada_peserta_didik')
    def _compute_jumlah_skor(self):
        for rec in self:
            rec.jumlah_skor = rec.nilai_total_komunikasi + rec.nilai_total_kepercayaan_dalam_memberikan_pendidikan_kepada_peserta_didik

    @api.depends('jumlah_indikator','skor_maksimum','jumlah_skor')
    def _compute_nilai_kinerja(self):
        for rec in self:
            rec.nilai_kinerja= (rec.jumlah_skor / rec.skor_maksimum) * 100

    # field buat pembagi
    pembagi = fields.Float(string='Pembagi', default=1, readonly=True)