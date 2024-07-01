from odoo import _, api, fields, models
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT




class PenilaianTemanSejawat(models.Model):
    _name = 'penilaian.teman.sejawat'
    _description = 'Model untuk tabel data penilaian guru teman sejawat'

    name = fields.Date(string='Tanggal Penilaian', default=datetime.now(), required=True)
    nama_responden = fields.Char(string='Nama Responden', default=lambda self: self.env.user.name, readonly=True)
    jabatan = fields.Char(string='Jabatan', default='Guru', readonly=True)
    creator_id = fields.Many2one('res.users', string='Creator', default=lambda self: self.env.user, readonly=True)
    data_guru_id = fields.Many2one(comodel_name='data.guru', string='Guru yang di nilai', required=True, ondelete="cascade")

    # ini kuisioner di dalam notebook :
    #1. Perilaku Guru Sehari-hari
    a = fields.Selection(string="Guru mentaati peraturan yang berlaku di sekolah..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    b = fields.Selection(string="Guru bekerja sesuai jadwal yang ditetapkan..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    c = fields.Selection(string="Guru berpakaian rapi dan/atau sopan..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    d = fields.Selection(string="Guru rajin mengikuti upacara bendera..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    e = fields.Selection(string="Guru berprilaku baik terhadap saya dan guru lain..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    f = fields.Selection(string="Guru bersedia menerima kritik dan saran dari saya atau guru lain..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    g = fields.Selection(string="Guru dapat menjadi teladan bagi saya dan teman-teman..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    h = fields.Selection(string="Guru pandai mengendalikan diri..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    i = fields.Selection(string="Guru ikut aktif menjaga lingkungan sekolah bebas dari asap rokok..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    j = fields.Selection(string="Guru berpartisipasi aktif dalam kegiatan ekstrakurikuler..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    k = fields.Selection(string="Guru berpartisispasi aktif dalam kegiatan peningkatan prestasi sekolah..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
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
    nilai_d = fields.Integer(string='',compute="compute_nilai_d")
    @api.depends('d')
    def compute_nilai_d(self):
        for rec in self:
            if rec.d == 'sering':
                rec.nilai_d = 2
            elif rec.d == 'kadang-kadang':
                rec.nilai_d = 1
            else:
                rec.nilai_d = 0
    nilai_e = fields.Integer(string='',compute="compute_nilai_e")
    @api.depends('e')
    def compute_nilai_e(self):
        for rec in self:
            if rec.e == 'sering':
                rec.nilai_e = 2
            elif rec.e == 'kadang-kadang':
                rec.nilai_e = 1
            else:
                rec.nilai_e = 0
    nilai_f = fields.Integer(string='',compute="compute_nilai_f")
    @api.depends('f')
    def compute_nilai_f(self):
        for rec in self:
            if rec.f == 'sering':
                rec.nilai_f = 2
            elif rec.f == 'kadang-kadang':
                rec.nilai_f = 1
            else:
                rec.nilai_f = 0
    nilai_g = fields.Integer(string='',compute="compute_nilai_g")
    @api.depends('g')
    def compute_nilai_g(self):
        for rec in self:
            if rec.g == 'sering':
                rec.nilai_g = 2
            elif rec.g == 'kadang-kadang':
                rec.nilai_g = 1
            else:
                rec.nilai_g = 0
    nilai_h = fields.Integer(string='',compute="compute_nilai_h")
    @api.depends('h')
    def compute_nilai_h(self):
        for rec in self:
            if rec.h == 'sering':
                rec.nilai_h = 2
            elif rec.h == 'kadang-kadang':
                rec.nilai_h = 1
            else:
                rec.nilai_h = 0
    nilai_i = fields.Integer(string='',compute="compute_nilai_i")
    @api.depends('i')
    def compute_nilai_i(self):
        for rec in self:
            if rec.i == 'sering':
                rec.nilai_i = 2
            elif rec.i == 'kadang-kadang':
                rec.nilai_i = 1
            else:
                rec.nilai_i = 0
    nilai_j = fields.Integer(string='',compute="compute_nilai_j")
    @api.depends('j')
    def compute_nilai_j(self):
        for rec in self:
            if rec.j == 'sering':
                rec.nilai_j = 2
            elif rec.j == 'kadang-kadang':
                rec.nilai_j = 1
            else:
                rec.nilai_j = 0
    nilai_k = fields.Integer(string='',compute="compute_nilai_k")
    @api.depends('k')
    def compute_nilai_k(self):
        for rec in self:
            if rec.k == 'sering':
                rec.nilai_k = 2
            elif rec.k == 'kadang-kadang':
                rec.nilai_k = 1
            else:
                rec.nilai_k = 0
                
    nilai_total_perilaku_guru_sehari_hari = fields.Float(string='Nilai Total', compute='compute_nilai_total_perilaku_guru_sehari_hari')
    @api.depends('nilai_a','nilai_b','nilai_c','nilai_d','nilai_e','nilai_f','nilai_g','nilai_h','nilai_i','nilai_j','nilai_k')
    def compute_nilai_total_perilaku_guru_sehari_hari(self):
        for rec in self:
            rec.nilai_total_perilaku_guru_sehari_hari = rec.nilai_a + rec.nilai_b + rec.nilai_c + rec.nilai_d + rec.nilai_e + rec.nilai_f + rec.nilai_g + rec.nilai_h + rec.nilai_i + rec.nilai_j + rec.nilai_k
    
    #2. Hubungan Guru Dengan Teman
    a1 = fields.Selection(string="Guru bersikap ramah kepada saya atau orang lain..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    b1 = fields.Selection(string="Guru berbahasa santun kepada saya atau orang lain..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    c1 = fields.Selection(string="Guru memberi motivasi kepada saya atau teman-teman guru lain..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    d1 = fields.Selection(string="Guru pandai berkomunikasi secara lisan atau tertulis..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    e1 = fields.Selection(string="Guru memotivasi diri dan rekan sejawat secara aktif dan kreatif dalam melaksanakan proses pendidikan..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    f1 = fields.Selection(string="Guru menciptakan suasana kekeluargaan di dalam dan luar sekolah..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    g1 = fields.Selection(string="Guru mudah bekerjasama dengan saya atau guru lainnya..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    h1 = fields.Selection(string="Guru bersedia diajak berdikusi tentang segala hal terkait kepentingan peserta didik dan sekolah..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    i1 = fields.Selection(string="Guru bersedia membantu menyelesaikan masalah saya dan guru lainnya..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    j1 = fields.Selection(string="Guru menghargai kemampuan saya dan guru lainnya..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])

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
    nilai_f1 = fields.Integer(string='',compute="compute_nilai_f1")
    @api.depends('f1')
    def compute_nilai_f1(self):
        for rec in self:
            if rec.f1 == 'sering':
                rec.nilai_f1 = 2
            elif rec.f1 == 'kadang-kadang':
                rec.nilai_f1 = 1
            else:
                rec.nilai_f1 = 0
    nilai_g1 = fields.Integer(string='',compute="compute_nilai_g1")
    @api.depends('g1')
    def compute_nilai_g1(self):
        for rec in self:
            if rec.g1 == 'sering':
                rec.nilai_g1 = 2
            elif rec.g1 == 'kadang-kadang':
                rec.nilai_g1 = 1
            else:
                rec.nilai_g1 = 0
    nilai_h1 = fields.Integer(string='',compute="compute_nilai_h1")
    @api.depends('h1')
    def compute_nilai_h1(self):
        for rec in self:
            if rec.h1 == 'sering':
                rec.nilai_h1 = 2
            elif rec.h1 == 'kadang-kadang':
                rec.nilai_h1 = 1
            else:
                rec.nilai_h1 = 0
    nilai_i1 = fields.Integer(string='',compute="compute_nilai_i1")
    @api.depends('i1')
    def compute_nilai_i1(self):
        for rec in self:
            if rec.i1 == 'sering':
                rec.nilai_i1 = 2
            elif rec.i1 == 'kadang-kadang':
                rec.nilai_i1 = 1
            else:
                rec.nilai_i1 = 0
    nilai_j1 = fields.Integer(string='',compute="compute_nilai_j1")
    @api.depends('j1')
    def compute_nilai_j1(self):
        for rec in self:
            if rec.j1 == 'sering':
                rec.nilai_j1 = 2
            elif rec.j1 == 'kadang-kadang':
                rec.nilai_j1 = 1
            else:
                rec.nilai_j1 = 0
                
    nilai_total_hubungan_guru_dengan_teman = fields.Float(string='Nilai Total', compute='compute_nilai_total_hubungan_guru_dengan_teman')
    @api.depends('nilai_a1','nilai_b1','nilai_c1','nilai_d1','nilai_e1','nilai_f1','nilai_g1','nilai_h1','nilai_i1','nilai_j1')
    def compute_nilai_total_hubungan_guru_dengan_teman(self):
        for rec in self:
            rec.nilai_total_hubungan_guru_dengan_teman = rec.nilai_a1 + rec.nilai_b1 + rec.nilai_c1 + rec.nilai_d1 + rec.nilai_e1 + rec.nilai_f1 + rec.nilai_g1 + rec.nilai_h1 + rec.nilai_i1 + rec.nilai_j1 
    
    #3. Perilaku Profesional Guru
    a2 = fields.Selection(string="Guru memiliki kretivitas dalam pembelajaran..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    b2 = fields.Selection(string="Guru memiliki pengetahuan dan keterampilan Teknologi Informasi (TI) yang memadai..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    c2 = fields.Selection(string="Guru memiliki perangkat pembelajaran yang lengkap..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    d2 = fields.Selection(string="Guru ada di sekolah meskipun  tidak mengajar di kelas..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    e2 = fields.Selection(string="Guru memulai  pembelajaran tepat waktu..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    f2 = fields.Selection(string="Guru mengakhiri pembelajaran tepat waktu..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    g2 = fields.Selection(string="Guru memberikan tugas kepada peserta didik apa bila berhalangan hadir untuk mengajar..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    h2 = fields.Selection(string="Guru memberi informasi kepada saya atau guru lain jika berhalangan hadir untuk mengajar..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    i2 = fields.Selection(string="Guru memperlakukan peserta didik dengan penuh kasih sayang..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])

    # Nilai per kategory 
    nilai_a2 = fields.Integer(string='',compute="compute_nilai_a2")
    @api.depends('a2')
    def compute_nilai_a2(self):
        for rec in self:
            if rec.a2 == 'sering':
                rec.nilai_a2 = 2
            elif rec.a2 == 'kadang-kadang':
                rec.nilai_a2 = 1
            else:
                rec.nilai_a2 = 0
    
    nilai_b2 = fields.Integer(string='',compute="compute_nilai_b2")
    @api.depends('b2')
    def compute_nilai_b2(self):
        for rec in self:
            if rec.b2 == 'sering':
                rec.nilai_b2 = 2
            elif rec.b2 == 'kadang-kadang':
                rec.nilai_b2 = 1
            else:
                rec.nilai_b2 = 0
    nilai_c2 = fields.Integer(string='',compute="compute_nilai_c2")
    @api.depends('c2')
    def compute_nilai_c2(self):
        for rec in self:
            if rec.c2 == 'sering':
                rec.nilai_c2 = 2
            elif rec.c2 == 'kadang-kadang':
                rec.nilai_c2 = 1
            else:
                rec.nilai_c2 = 0
    nilai_d2 = fields.Integer(string='',compute="compute_nilai_d2")
    @api.depends('d2')
    def compute_nilai_d2(self):
        for rec in self:
            if rec.d2 == 'sering':
                rec.nilai_d2 = 2
            elif rec.d2 == 'kadang-kadang':
                rec.nilai_d2 = 1
            else:
                rec.nilai_d2 = 0
    nilai_e2 = fields.Integer(string='',compute="compute_nilai_e2")
    @api.depends('e2')
    def compute_nilai_e2(self):
        for rec in self:
            if rec.e2 == 'sering':
                rec.nilai_e2 = 2
            elif rec.e2 == 'kadang-kadang':
                rec.nilai_e2 = 1
            else:
                rec.nilai_e2 = 0
    nilai_f2 = fields.Integer(string='',compute="compute_nilai_f2")
    @api.depends('f2')
    def compute_nilai_f2(self):
        for rec in self:
            if rec.f2 == 'sering':
                rec.nilai_f2 = 2
            elif rec.f2 == 'kadang-kadang':
                rec.nilai_f2 = 1
            else:
                rec.nilai_f2 = 0
    nilai_g2 = fields.Integer(string='',compute="compute_nilai_g2")
    @api.depends('g2')
    def compute_nilai_g2(self):
        for rec in self:
            if rec.g2 == 'sering':
                rec.nilai_g2 = 2
            elif rec.g2 == 'kadang-kadang':
                rec.nilai_g2 = 1
            else:
                rec.nilai_g2 = 0
    nilai_h2 = fields.Integer(string='',compute="compute_nilai_h2")
    @api.depends('h2')
    def compute_nilai_h2(self):
        for rec in self:
            if rec.h2 == 'sering':
                rec.nilai_h2 = 2
            elif rec.h2 == 'kadang-kadang':
                rec.nilai_h2 = 1
            else:
                rec.nilai_h2 = 0
    nilai_i2 = fields.Integer(string='',compute="compute_nilai_i2")
    @api.depends('i2')
    def compute_nilai_i2(self):
        for rec in self:
            if rec.i2 == 'sering':
                rec.nilai_i2 = 2
            elif rec.i2 == 'kadang-kadang':
                rec.nilai_i2 = 1
            else:
                rec.nilai_i2 = 0
                
    nilai_total_perilaku_profesional_guru = fields.Float(string='Nilai Total', compute='compute_nilai_total_perilaku_profesional_guru')
    @api.depends('nilai_a2','nilai_b2','nilai_c2','nilai_d2','nilai_e2','nilai_f2','nilai_g2','nilai_h2','nilai_i2')
    def compute_nilai_total_perilaku_profesional_guru(self):
        for rec in self:
            rec.nilai_total_perilaku_profesional_guru = rec.nilai_a2 + rec.nilai_b2 + rec.nilai_c2 + rec.nilai_d2 + rec.nilai_e2 + rec.nilai_f2 + rec.nilai_g2 + rec.nilai_h2 + rec.nilai_i2
    
    
    # PERHITUNGAN NILAI KINERJA
    jumlah_indikator = fields.Float(string='Jumlah Indikator', readonly=True, default=30)
    skor_maksimum = fields.Float(string='Skor Maksimum', compute="_compute_skor_maksimum")
    jumlah_skor = fields.Float(string='Jumlah Skor', compute="_compute_jumlah_skor")
    nilai_kinerja = fields.Float(string='Nilai Kinerja', compute="_compute_nilai_kinerja")
    
    
    @api.depends('jumlah_indikator')
    def _compute_skor_maksimum(self):
        for rec in self:
            rec.skor_maksimum = rec.jumlah_indikator * 2

    
    @api.depends('nilai_total_perilaku_guru_sehari_hari','nilai_total_hubungan_guru_dengan_teman','nilai_total_perilaku_profesional_guru')
    def _compute_jumlah_skor(self):
        for rec in self:
            rec.jumlah_skor = rec.nilai_total_perilaku_guru_sehari_hari + rec.nilai_total_hubungan_guru_dengan_teman + rec.nilai_total_perilaku_profesional_guru

    @api.depends('jumlah_indikator','skor_maksimum','jumlah_skor')
    def _compute_nilai_kinerja(self):
        for rec in self:
            rec.nilai_kinerja= (rec.jumlah_skor / rec.skor_maksimum) * 100

    # field buat pembagi
    pembagi = fields.Float(string='Pembagi', default=1, readonly=True)
    
    