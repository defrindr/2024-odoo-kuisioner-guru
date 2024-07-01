from odoo import _, api, fields, models
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT




class PenilaianPesertaDidik(models.Model):
    _name = 'penilaian.peserta.didik'
    _description = 'Model untuk tabel data penilaian peserta didik'

    name = fields.Date(string='Tanggal Penilaian', default=datetime.now(), required="True")
    nama_responden = fields.Char(string='Nama Responden', required=True)
    jabatan = fields.Char(string='Jabatan', default='Peserta Didik/Murit', readonly=True)
    data_guru_id = fields.Many2one(comodel_name='data.guru', string='Guru yang di nilai', required=True, ondelete="cascade")

    # ini kuisioner di dalam notebook :
    #1. Penguasaan Materi
    a = fields.Selection(string="Guru menyampaikan materi pelajaran dengan contoh dalam kehidupan sehari-hari..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    b = fields.Selection(string="Guru menjelaskan materi pelajaran dari buku paket dan sumber belajar lainnya..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    c = fields.Selection(string="Guru memberikan contoh atau permasalahan yang berhubungan dengan keadaan saat ini..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    d = fields.Selection(string="Guru menjawab pertanyaan dengan jelas..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    e = fields.Selection(string="Guru menjawab pertanyaan dengan benar..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    f = fields.Selection(string="Guru mengajar sesuai dengan materi pelajaran..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])

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
                
    nilai_total_penguasaan_materi = fields.Float(string='Nilai Total', compute='compute_nilai_total_penguasaan_materi')
    @api.depends('nilai_a','nilai_b','nilai_c','nilai_d','nilai_e','nilai_f')
    def compute_nilai_total_penguasaan_materi(self):
        for rec in self:
            rec.nilai_total_penguasaan_materi = rec.nilai_a + rec.nilai_b + rec.nilai_c + rec.nilai_d + rec.nilai_e + rec.nilai_f
    
    #2. Kemahiran Dalam Mengajar
    a1 = fields.Selection(string="Guru menyampaikan kegiatan yang akan dilakukan selama pembelajaran..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    b1 = fields.Selection(string="Guru memberikan motivasi kepada saya dan teman-teman..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    c1 = fields.Selection(string="Guru menyampaikan materi pelajaran dengan mudah dimengerti..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    d1 = fields.Selection(string="Guru mengajar dengan cara yang bervariasi misalnya diskusi, demonstrasi, tanya jawab, ceramah, dll..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    e1 = fields.Selection(string="Guru berbicara dengan jelas ketika menyampaikan materi pelajaran..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    f1 = fields.Selection(string="Guru meminta belajar secara berkelompok..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    g1 = fields.Selection(string="Guru mengajar dengan cara yang menyenangkan dan menarik..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    h1 = fields.Selection(string="Guru terampil menggunakan alat bantu saat mengajar..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    i1 = fields.Selection(string="Guru membimbing saya dan teman-teman ketika mengalami kesulitan..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    j1 = fields.Selection(string="Guru membuat suasana nyaman saat melaksanakan pembelajaran..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    k1 = fields.Selection(string="Guru memberi kesempatan kepada saya dan teman-teman untuk bertanya atau menjawab..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    l1 = fields.Selection(string="Guru menghargai kemampuan saya dan teman-teman..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    m1 = fields.Selection(string="Guru memberitahukan nilai hasil belajar..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    n1 = fields.Selection(string="Guru memberikan tugas dalam pembelajaran..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])

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
    nilai_k1 = fields.Integer(string='',compute="compute_nilai_k1")
    @api.depends('k1')
    def compute_nilai_k1(self):
        for rec in self:
            if rec.k1 == 'sering':
                rec.nilai_k1 = 2
            elif rec.k1 == 'kadang-kadang':
                rec.nilai_k1 = 1
            else:
                rec.nilai_k1 = 0
    nilai_l1 = fields.Integer(string='',compute="compute_nilai_l1")
    @api.depends('l1')
    def compute_nilai_l1(self):
        for rec in self:
            if rec.l1 == 'sering':
                rec.nilai_l1 = 2
            elif rec.l1 == 'kadang-kadang':
                rec.nilai_l1 = 1
            else:
                rec.nilai_l1 = 0
    nilai_m1 = fields.Integer(string='',compute="compute_nilai_m1")
    @api.depends('m1')
    def compute_nilai_m1(self):
        for rec in self:
            if rec.m1 == 'sering':
                rec.nilai_m1 = 2
            elif rec.m1 == 'kadang-kadang':
                rec.nilai_m1 = 1
            else:
                rec.nilai_m1 = 0
    nilai_n1 = fields.Integer(string='',compute="compute_nilai_n1")
    @api.depends('n1')
    def compute_nilai_n1(self):
        for rec in self:
            if rec.n1 == 'sering':
                rec.nilai_n1 = 2
            elif rec.n1 == 'kadang-kadang':
                rec.nilai_n1 = 1
            else:
                rec.nilai_n1 = 0
                
    nilai_total_kemahiran_dalam_mengajar = fields.Float(string='Nilai Total', compute='compute_nilai_total_kemahiran_dalam_mengajar')
    @api.depends('nilai_a1','nilai_b1','nilai_c1','nilai_d1','nilai_e1','nilai_f1','nilai_g1','nilai_h1','nilai_i1','nilai_j1','nilai_k1','nilai_l1','nilai_m1','nilai_n1')
    def compute_nilai_total_kemahiran_dalam_mengajar(self):
        for rec in self:
            rec.nilai_total_kemahiran_dalam_mengajar= rec.nilai_a1 + rec.nilai_b1 + rec.nilai_c1 + rec.nilai_d1 + rec.nilai_e1 + rec.nilai_f1 + rec.nilai_g1 + rec.nilai_h1 + rec.nilai_i1 + rec.nilai_j1 + rec.nilai_k1 + rec.nilai_l1 + rec.nilai_m1 + rec.nilai_n1 

    #2. Perilaku Guru Sehari-hari
    a2 = fields.Selection(string="Guru mengajak saya dan teman-teman untuk berperilaku baik..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    b2 = fields.Selection(string="Guru memberi contoh perilaku yang sesuai aturan..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    c2 = fields.Selection(string="Guru menjalankan ibadah sesuai dengan ajaran agamanya..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    d2 = fields.Selection(string="Guru berpakaian rapi sesuai aturan sekolah..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    e2 = fields.Selection(string="Guru menghargai perbedaan asal, suku, ras dan agama..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    f2 = fields.Selection(string="Guru berpakaian sopan..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    g2 = fields.Selection(string="Guru berbicara dengan santun..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    h2 = fields.Selection(string="Guru ramah..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    i2 = fields.Selection(string="Guru sabar..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    j2 = fields.Selection(string="Guru memulai pembelajaran tepat waktu..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    k2 = fields.Selection(string="Guru mengakhiri pembelajaran tepat waktu..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    l2 = fields.Selection(string="Guru memberikan tugas apabila berhalangan hadir..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    m2 = fields.Selection(string="Guru menjaga lingkungan sekolah tanpa asap rokok..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    n2 = fields.Selection(string="Guru menjaga kebersihan lingkungan sekolah..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    o2 = fields.Selection(string="Guru memulai dan mengakhiri pembelajaran dengan berdoa bersama..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
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
    nilai_j2 = fields.Integer(string='',compute="compute_nilai_j2")
    @api.depends('j2')
    def compute_nilai_j2(self):
        for rec in self:
            if rec.j2 == 'sering':
                rec.nilai_j2 = 2
            elif rec.j2 == 'kadang-kadang':
                rec.nilai_j2 = 1
            else:
                rec.nilai_j2 = 0
    nilai_k2 = fields.Integer(string='',compute="compute_nilai_k2")
    @api.depends('k2')
    def compute_nilai_k2(self):
        for rec in self:
            if rec.k2 == 'sering':
                rec.nilai_k2 = 2
            elif rec.k2 == 'kadang-kadang':
                rec.nilai_k2 = 1
            else:
                rec.nilai_k2 = 0
    nilai_l2 = fields.Integer(string='',compute="compute_nilai_l2")
    @api.depends('l2')
    def compute_nilai_l2(self):
        for rec in self:
            if rec.l2 == 'sering':
                rec.nilai_l2 = 2
            elif rec.l2 == 'kadang-kadang':
                rec.nilai_l2 = 1
            else:
                rec.nilai_l2 = 0
    nilai_m2 = fields.Integer(string='',compute="compute_nilai_m2")
    @api.depends('m2')
    def compute_nilai_m2(self):
        for rec in self:
            if rec.m2 == 'sering':
                rec.nilai_m2 = 2
            elif rec.m2 == 'kadang-kadang':
                rec.nilai_m2 = 1
            else:
                rec.nilai_m2 = 0
    nilai_n2 = fields.Integer(string='',compute="compute_nilai_n2")
    @api.depends('n2')
    def compute_nilai_n2(self):
        for rec in self:
            if rec.n2 == 'sering':
                rec.nilai_n2 = 2
            elif rec.n2 == 'kadang-kadang':
                rec.nilai_n2 = 1
            else:
                rec.nilai_n2 = 0
    nilai_o2 = fields.Integer(string='',compute="compute_nilai_o2")
    @api.depends('o2')
    def compute_nilai_o2(self):
        for rec in self:
            if rec.o2 == 'sering':
                rec.nilai_o2 = 2
            elif rec.o2 == 'kadang-kadang':
                rec.nilai_o2 = 1
            else:
                rec.nilai_o2 = 0
                
    nilai_total_perilaku_guru_sehari_hari = fields.Float(string='Nilai Total', compute='compute_nilai_total_perilaku_guru_sehari_hari')
    @api.depends('nilai_a2','nilai_b2','nilai_c2','nilai_d2','nilai_e2','nilai_f2','nilai_g2','nilai_h2','nilai_i2','nilai_j2','nilai_k2','nilai_l2','nilai_m2','nilai_n2','nilai_o2')
    def compute_nilai_total_perilaku_guru_sehari_hari(self):
        for rec in self:
            rec.nilai_total_perilaku_guru_sehari_hari = rec.nilai_a2 + rec.nilai_b2 + rec.nilai_c2 + rec.nilai_d2 + rec.nilai_e2 + rec.nilai_f2 + rec.nilai_g2 + rec.nilai_h2 + rec.nilai_i2 + rec.nilai_j2 + rec.nilai_k2 + rec.nilai_l2 + rec.nilai_m2 + rec.nilai_n2 + rec.nilai_o2 

    #3. Hubungan Sosial Dengan Peserta Didik
    a3 = fields.Selection(string="Guru memperhatikan kebutuhan belajar saya dan teman-teman..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    b3 = fields.Selection(string="Guru menyebutkan nama saya dan teman-teman selama kegiatan pembelajaran atau  kegiatan lainnya)..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    c3 = fields.Selection(string="Guru memberi perhatian kepada saya dan teman-teman..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    d3 = fields.Selection(string="Guru memilihara komunikasi yang baik dengan semua peserta didik..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    e3 = fields.Selection(string="Guru mudah dihubungi pada saat diperlukan untuk diskusi..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    f3 = fields.Selection(string="Guru akrab dengan saya dan teman-teman..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    g3 = fields.Selection(string="Guru ikut serta dalam berbagai macam kegiatan sekolah (upacara, kegiatan keagamaan, senam bersama)..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])

    # Nilai per kategory
    nilai_a3 = fields.Integer(string='',compute="compute_nilai_a3")
    @api.depends('a3')
    def compute_nilai_a3(self):
        for rec in self:
            if rec.a3 == 'sering':
                rec.nilai_a3 = 2
            elif rec.a3 == 'kadang-kadang':
                rec.nilai_a3 = 1
            else:
                rec.nilai_a3 = 0
    
    nilai_b3 = fields.Integer(string='',compute="compute_nilai_b3")
    @api.depends('b3')
    def compute_nilai_b3(self):
        for rec in self:
            if rec.b3 == 'sering':
                rec.nilai_b3 = 2
            elif rec.b3 == 'kadang-kadang':
                rec.nilai_b3 = 1
            else:
                rec.nilai_b3 = 0
    nilai_c3 = fields.Integer(string='',compute="compute_nilai_c3")
    @api.depends('c3')
    def compute_nilai_c3(self):
        for rec in self:
            if rec.c3 == 'sering':
                rec.nilai_c3 = 2
            elif rec.c3 == 'kadang-kadang':
                rec.nilai_c3 = 1
            else:
                rec.nilai_c3 = 0
    nilai_d3 = fields.Integer(string='',compute="compute_nilai_d3")
    @api.depends('d3')
    def compute_nilai_d3(self):
        for rec in self:
            if rec.d3 == 'sering':
                rec.nilai_d3 = 2
            elif rec.d3 == 'kadang-kadang':
                rec.nilai_d3 = 1
            else:
                rec.nilai_d3 = 0
    nilai_e3 = fields.Integer(string='',compute="compute_nilai_e3")
    @api.depends('e3')
    def compute_nilai_e3(self):
        for rec in self:
            if rec.e3 == 'sering':
                rec.nilai_e3 = 2
            elif rec.e3 == 'kadang-kadang':
                rec.nilai_e3 = 1
            else:
                rec.nilai_e3 = 0
    nilai_f3 = fields.Integer(string='',compute="compute_nilai_f3")
    @api.depends('f3')
    def compute_nilai_f3(self):
        for rec in self:
            if rec.f3 == 'sering':
                rec.nilai_f3 = 2
            elif rec.f3 == 'kadang-kadang':
                rec.nilai_f3 = 1
            else:
                rec.nilai_f3 = 0
    nilai_g3 = fields.Integer(string='',compute="compute_nilai_g3")
    @api.depends('g3')
    def compute_nilai_g3(self):
        for rec in self:
            if rec.g3 == 'sering':
                rec.nilai_g3 = 2
            elif rec.g3 == 'kadang-kadang':
                rec.nilai_g3 = 1
            else:
                rec.nilai_g3 = 0
                
    nilai_total_hubungan_sosial_dengan_peserta_didik = fields.Float(string='Nilai Total', compute='compute_nilai_total_hubungan_sosial_dengan_peserta_didik')
    @api.depends('nilai_a3','nilai_b3','nilai_c3','nilai_d3','nilai_e3','nilai_f3','nilai_g3')
    def compute_nilai_total_hubungan_sosial_dengan_peserta_didik(self):
        for rec in self:
            rec.nilai_total_hubungan_sosial_dengan_peserta_didik = rec.nilai_a3 + rec.nilai_b3 + rec.nilai_c3 + rec.nilai_d3 + rec.nilai_e3 + rec.nilai_f3 + rec.nilai_g3

    # PERHITUNGAN NILAI KINERJA
    jumlah_indikator = fields.Float(string='Jumlah Indikator', readonly=True, default=42)
    skor_maksimum = fields.Float(string='Skor Maksimum', compute="_compute_skor_maksimum")
    jumlah_skor = fields.Float(string='Jumlah Skor', compute="_compute_jumlah_skor")
    nilai_kinerja = fields.Float(string='Nilai Kinerja', compute="_compute_nilai_kinerja")
    
    
    @api.depends('jumlah_indikator')
    def _compute_skor_maksimum(self):
        for rec in self:
            rec.skor_maksimum = rec.jumlah_indikator * 2

    
    @api.depends('nilai_total_penguasaan_materi','nilai_total_kemahiran_dalam_mengajar','nilai_total_perilaku_guru_sehari_hari','nilai_total_hubungan_sosial_dengan_peserta_didik')
    def _compute_jumlah_skor(self):
        for rec in self:
            rec.jumlah_skor = rec.nilai_total_penguasaan_materi + rec.nilai_total_kemahiran_dalam_mengajar + rec.nilai_total_perilaku_guru_sehari_hari + rec.nilai_total_hubungan_sosial_dengan_peserta_didik

    @api.depends('jumlah_indikator','skor_maksimum','jumlah_skor')
    def _compute_nilai_kinerja(self):
        for rec in self:
            rec.nilai_kinerja= (rec.jumlah_skor / rec.skor_maksimum) * 100

    # field buat pembagi
    pembagi = fields.Float(string='Pembagi', default=1, readonly=True)