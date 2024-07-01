from odoo import api, fields, models
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT



class PenilaianKepalaSekolah(models.Model):
    _name = 'penilaian.kepala.sekolah'
    _description = 'Model untuk tabel data penilaian dari kepala sekolah'

    name = fields.Date(string='Tanggal Penilaian', default=datetime.now(), required=True)
    nama_responden = fields.Char(string='Nama Responden', default="Astutik, S.Pd.", required="True")
    jabatan = fields.Char(string='Jabatan', default='Kepala Sekolah', readonly=True)
    data_guru_id = fields.Many2one(comodel_name='data.guru', string='Guru yang di nilai', required="True", ondelete="cascade")
    # ini kuisioner di dalam notebook :
    
#1. Mengenal karakteristik peserta didik
    a = fields.Selection(string="Guru dapat khusus tentang peserta didik (perihal kelebihan, kekurangan, kelemahan, kecenderungan perilaku mengganggu) yang perlu memperoleh perhatian guru..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    b = fields.Selection(string="Guru dapat Mencatat kemajuan dan perkembangan peserta didik..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    c = fields.Selection(string="Guru dapat menjelaskan kemampuan belajar empat peserta didik yang ditunjuk secara acak..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    d = fields.Selection(string="Guru mengecek kahadiran siswa dan Memberi motivasi kepada peserta didik..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    e = fields.Selection(string="Guru dapat menyebutkan peserta didik yang paling pandai/lemah di kelasnya..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    f = fields.Selection(string="Guru dapat menjelaskan langkah-langkah (yang sifatnya pedagogis) dalam merancang pembelajaran untuk peserta didik yang beragam..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    g = fields.Selection(string="Guru dapat memberi klasifikasi umum kemampuan belajar peserta didik di kelasnya (berdasarkan potensi kecerdasannya)..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    h = fields.Selection(string="Guru mempergunakan alat/media yang tepat sehingga semua peserta didik dapat mengikuti kegiatan pembelajaran secara optimal..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])

    # Nilai per kategory dari karakteristik peserta didik
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
                
    nilai_total_karakteristik_peserta_didik = fields.Float(string='Nilai Total', compute='compute_nilai_total_karakteristik_peserta_didik')
    @api.depends('nilai_a','nilai_b','nilai_c','nilai_d','nilai_e','nilai_f','nilai_g','nilai_h')
    def compute_nilai_total_karakteristik_peserta_didik(self):
        for rec in self:
            rec.nilai_total_karakteristik_peserta_didik = rec.nilai_a + rec.nilai_b + rec.nilai_c + rec.nilai_d + rec.nilai_e + rec.nilai_f + rec.nilai_g + rec.nilai_h
    
#2. Penguasaan Teori Belajar dan prinsip" pembelajaran yg mendidik
    a1 = fields.Selection(string="Guru dapat mengajukan pertanyaan-pertanyaan yang mengaitkan pengetahuan sebelumnya dengan materi yang akan dipelajari..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    b1 = fields.Selection(string="Guru dapat menyampaikan kompetensi yang akan dicapai dalam kegiatan pembelajaran..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    c1 = fields.Selection(string="Guru dapat mengimplementasikan metode/teknik pembelajaran yang bervariasi untuk memberi kesempatan peserta didik menguasai materi sesuai kemampuan masing-masing..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    d1 = fields.Selection(string="Guru dapat memberi kesempatan peserta didik untuk bertanya, berdiskusi/sharing dengan teman-temannya agar penguasai materi pembelajaran lebih merata..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    e1 = fields.Selection(string="Guru dapat menjelaskan langkah-langkah penentuan KKM denngan mempertimbangkan kemampuan rata-rata peserta didik..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    f1 = fields.Selection(string="Guru tanggap apabila ada tanda-tanda peserta didik tertentu kurang atau belam memahami materi pembelajaran..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    g1 = fields.Selection(string="Guru mencatat hal-hal penting terkait dengan problem pembelajaran untuk ditindaklanjuti dan/atau diperbaiki pada rencana pembelajaran selanjutnya..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    h1 = fields.Selection(string="Guru dapat menjelaskan kaitan rasional antara materi ajar, tujuan pembelajaran, indikator pencapaian kompetensi, kompetensi dasar dan standar kompetensi..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])

    # Nilai Penguasaan Teori Belajar dan prinsip" pembelajaran yg mendidik
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
                
    nilai_total_teori_belajar_dan_prinsip_pembelajaran_yg_mendidik = fields.Float(string='Nilai Total', compute='compute_nilai_total_teori_belajar_dan_prinsip_pembelajaran_yg_mendidik')
    @api.depends('nilai_a1','nilai_b1','nilai_c1','nilai_d1','nilai_e1','nilai_f1','nilai_g1','nilai_h1')
    def compute_nilai_total_teori_belajar_dan_prinsip_pembelajaran_yg_mendidik(self):
        for rec in self:
            rec.nilai_total_teori_belajar_dan_prinsip_pembelajaran_yg_mendidik = rec.nilai_a1 + rec.nilai_b1 + rec.nilai_c1 + rec.nilai_d1 + rec.nilai_e1 + rec.nilai_f1 + rec.nilai_g1 + rec.nilai_h1


#3. Penilaian Pengembangan Kurikulum
    a2 = fields.Selection(string="Materi pembelajaran dirancang bisa dilaksanakan di kelas atau di luar kelas (seperti lab, bengkel dan sebagainya)..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    b2 = fields.Selection(string="Guru menyajikan materi pembelajaran secara runtut dan logis..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    c2 = fields.Selection(string="Guru membiasakan peserta didik menggunakan buku-buku dan sumber belajar yang lain di perpustakaan..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    d2 = fields.Selection(string="Guru mempergunakan buku ajar yang telah ditetapkan oleh Menteri..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    e2 = fields.Selection(string="Materi pembelajaran dikembangkan sesuai herarki dan struktur keilmuannya..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    f2 = fields.Selection(string="Materi pembelajaran dikembangkan mendukung tercapainya kompetensi lulusan..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    g2 = fields.Selection(string="Guru menyajikan materi pembelajaran sesuai kompetensi yang hendak dicapai..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    h2 = fields.Selection(string="Guru menjelaskan bagaimana silabus itu disusun berdasarkan hasil analisis SK-KD..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    i2 = fields.Selection(string="Guru menjelaskan bagaimana menyusun RPP sesuai silabus..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    j2 = fields.Selection(string="Guru mengaitkan materi pelajaran dengan kehidupan sehari-hari..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])

    # Nilai Pengembangan Kurikulum
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
                
    nilai_total_pengembangan_kurikulum = fields.Float(string='Nilai Total', compute='compute_nilai_total_pengembangan_kurikulum')
    @api.depends('nilai_a2','nilai_b2','nilai_c2','nilai_d2','nilai_e2','nilai_f2','nilai_g2','nilai_h2','nilai_i2','nilai_j2')
    def compute_nilai_total_pengembangan_kurikulum(self):
        for rec in self:
            rec.nilai_total_pengembangan_kurikulum = rec.nilai_a2 + rec.nilai_b2 + rec.nilai_c2 + rec.nilai_d2 + rec.nilai_e2 + rec.nilai_f2 + rec.nilai_g2 + rec.nilai_h2 + rec.nilai_i2 + rec.nilai_j2

# 4. Bertindak sesuai norma, agama, hukum, sosial dan kebudayaan nasional.
    a3 = fields.Selection(string="Guru menerapkan prinsip-prinsip Pancasila sebagai dasar ideologi bermasyarakat dan berbangsa..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    b3 = fields.Selection(string="Guru beretika sesuai karakter dan budaya bangsa..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    c3 = fields.Selection(string="Bekerja sama dengan teman sejawat secara wajar tanpa membedakan suku, agama, ras, golongan dan gender..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    d3 = fields.Selection(string="Berkolaborasi aktif dan dinamik (berat sama dipikul ringan sama dijinjing) dalam menyelesaikan tugas dan/atau permasalahan sekolah..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    e3 = fields.Selection(string="Menerima dan menghormati keberagaman dan perbedaan-perbedaan sebagai hal wajar..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    f3 = fields.Selection(string="Menghargai pendapat orang lain (baik sejawat, orangtua/wali, siswa atau yang lain-lain)..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    g3 = fields.Selection(string="Aktif terlibat dalam berbagai kapanitiaan/kepengurusan sekolah atau yang lebih tinggi di bidang pendidikan (seperti Pramuka, OSN, Paskribra, Dharmawanita dan lain-lain)..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    h3 = fields.Selection(string="Guru menjelaskan bagaimana pandangannya tentang perbedaan-perbedaan yang ada dalam masyarakat, baik karena perbedaan latar belakang budaya, suku atau agama..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])

    # Nilai Guru Bertindak sesuai norma, agama, hukum, sosial dan kebudayaan nasional.
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
    nilai_h3 = fields.Integer(string='',compute="compute_nilai_h3")
    @api.depends('h3')
    def compute_nilai_h3(self):
        for rec in self:
            if rec.h3 == 'sering':
                rec.nilai_h3 = 2
            elif rec.h3 == 'kadang-kadang':
                rec.nilai_h3 = 1
            else:
                rec.nilai_h3 = 0
                
    nilai_total_guru_bertindak_sesuai_norma_agama = fields.Float(string='Nilai Total', compute='compute_nilai_total_guru_bertindak_sesuai_norma_agama')
    @api.depends('nilai_a3','nilai_b3','nilai_c3','nilai_d3','nilai_e3','nilai_f3','nilai_g3','nilai_h3')
    def compute_nilai_total_guru_bertindak_sesuai_norma_agama(self):
        for rec in self:
            rec.nilai_total_guru_bertindak_sesuai_norma_agama  = rec.nilai_a3 + rec.nilai_b3 + rec.nilai_c3 + rec.nilai_d3 + rec.nilai_e3 + rec.nilai_f3 + rec.nilai_g3 + rec.nilai_h3


    #5. Penilaian Guru Menunjukkan pribadi yang dewasa dan teladan
    a4 = fields.Selection(string="Guru berbicara dengan pilihan kata dan ungkapan yang tepat dan mendidik sesuai perkembangan dan usia peserta didik..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    b4 = fields.Selection(string="Guru berpakaian rapi dan sopan sesuai kelayakan budaya, norma hukum dan keyakinan beragama..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    c4 = fields.Selection(string="Guru berperilaku terpuji sesuai tata krama yang berlaku dan keyakinan beragama..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    d4 = fields.Selection(string="Guru tidak melakukan hal-hal yang terindikasi melanggar norma, baik norma hukum, budaya atau agama..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    e4 = fields.Selection(string="Guru suka berbuat kebaikan untuk sesama, misalnya pada sejawat, orangtua/wali, peserta didik dan lain-lain..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    f4 = fields.Selection(string="Guru suka berbagai pengalaman dan informasi dengan teman sejawat (misalnya dalam rangka pengembangan keprofesian berkelanjutan)..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    g4 = fields.Selection(string="Guru menerima masukan (umpan balik) dari peserta didik terkait kegiatan pembelajaran (terutama dalam hal pemilihan strategi, metode/teknik dan gaya mengajar)..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    h4 = fields.Selection(string="Guru menjaga citra dan nama baik sekolah (dan lebih utama apabila dapat mengharumkan nama sekolah dengan kreatifitas dan prestasi yang dicapainya)..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    i4 = fields.Selection(string="Guru menerima dan melaksanakan tugas-tugas keluar mewakili sekolah, seperti mengikuti upacara bendera, mengikuti lomba guru dan lainsebagainya..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])
    j4 = fields.Selection(string="Guru melaksanakan tugas-tugas di luar sekolah sekolah, seperti diklat, menjadi nara sumber, mengikuti lomba antar guru atau yang lain-lain berdasarkan surat tugas atau ijin Kepala Sekolah..", selection=[('sering', 'Sering'), ('kadang-kadang', 'Kadang-kadang'),('tidak pernah','Tidak Pernah')])

    # Nilai Guru Menunjukkan pribadi yang dewasa dan teladan
    nilai_a4 = fields.Integer(string='',compute="compute_nilai_a4")
    @api.depends('a4')
    def compute_nilai_a4(self):
        for rec in self:
            if rec.a4 == 'sering':
                rec.nilai_a4 = 2
            elif rec.a4 == 'kadang-kadang':
                rec.nilai_a4 = 1
            else:
                rec.nilai_a4 = 0
    
    nilai_b4 = fields.Integer(string='',compute="compute_nilai_b4")
    @api.depends('b4')
    def compute_nilai_b4(self):
        for rec in self:
            if rec.b4 == 'sering':
                rec.nilai_b4 = 2
            elif rec.b4 == 'kadang-kadang':
                rec.nilai_b4 = 1
            else:
                rec.nilai_b4 = 0
    nilai_c4 = fields.Integer(string='',compute="compute_nilai_c4")
    @api.depends('c4')
    def compute_nilai_c4(self):
        for rec in self:
            if rec.c4 == 'sering':
                rec.nilai_c4 = 2
            elif rec.c4 == 'kadang-kadang':
                rec.nilai_c4 = 1
            else:
                rec.nilai_c4 = 0
    nilai_d4 = fields.Integer(string='',compute="compute_nilai_d4")
    @api.depends('d4')
    def compute_nilai_d4(self):
        for rec in self:
            if rec.d4 == 'sering':
                rec.nilai_d4 = 2
            elif rec.d4 == 'kadang-kadang':
                rec.nilai_d4 = 1
            else:
                rec.nilai_d4 = 0
    nilai_e4 = fields.Integer(string='',compute="compute_nilai_e4")
    @api.depends('e4')
    def compute_nilai_e4(self):
        for rec in self:
            if rec.e4 == 'sering':
                rec.nilai_e4 = 2
            elif rec.e4 == 'kadang-kadang':
                rec.nilai_e4 = 1
            else:
                rec.nilai_e4 = 0
    nilai_f4 = fields.Integer(string='',compute="compute_nilai_f4")
    @api.depends('f4')
    def compute_nilai_f4(self):
        for rec in self:
            if rec.f4 == 'sering':
                rec.nilai_f4 = 2
            elif rec.f4 == 'kadang-kadang':
                rec.nilai_f4 = 1
            else:
                rec.nilai_f4 = 0
    nilai_g4 = fields.Integer(string='',compute="compute_nilai_g4")
    @api.depends('g4')
    def compute_nilai_g4(self):
        for rec in self:
            if rec.g4 == 'sering':
                rec.nilai_g4 = 2
            elif rec.g4 == 'kadang-kadang':
                rec.nilai_g4 = 1
            else:
                rec.nilai_g4 = 0
    nilai_h4 = fields.Integer(string='',compute="compute_nilai_h4")
    @api.depends('h4')
    def compute_nilai_h4(self):
        for rec in self:
            if rec.h4 == 'sering':
                rec.nilai_h4 = 2
            elif rec.h4 == 'kadang-kadang':
                rec.nilai_h4 = 1
            else:
                rec.nilai_h4 = 0
    nilai_i4 = fields.Integer(string='',compute="compute_nilai_i4")
    @api.depends('i4')
    def compute_nilai_i4(self):
        for rec in self:
            if rec.i4 == 'sering':
                rec.nilai_i4 = 2
            elif rec.i4 == 'kadang-kadang':
                rec.nilai_i4 = 1
            else:
                rec.nilai_i4 = 0
    nilai_j4 = fields.Integer(string='',compute="compute_nilai_j4")
    @api.depends('j4')
    def compute_nilai_j4(self):
        for rec in self:
            if rec.j4 == 'sering':
                rec.nilai_j4 = 2
            elif rec.j4 == 'kadang-kadang':
                rec.nilai_j4 = 1
            else:
                rec.nilai_j4 = 0
                
    nilai_total_guru_menunjukan_pribadi_dewasa_dan_teladan = fields.Float(string='Nilai Total', compute='compute_nilai_total_guru_menunjukan_pribadi_dewasa_dan_teladan')
    @api.depends('nilai_a4','nilai_b4','nilai_c4','nilai_d4','nilai_e4','nilai_f4','nilai_g4','nilai_h4','nilai_i4','nilai_j4')
    def compute_nilai_total_guru_menunjukan_pribadi_dewasa_dan_teladan(self):
        for rec in self:
            rec.nilai_total_guru_menunjukan_pribadi_dewasa_dan_teladan = rec.nilai_a4 + rec.nilai_b4 + rec.nilai_c4 + rec.nilai_d4 + rec.nilai_e4 + rec.nilai_f4 + rec.nilai_g4 + rec.nilai_h4 + rec.nilai_i4 + rec.nilai_j4

    # PERHITUNGAN NILAI KINERJA
    jumlah_indikator = fields.Float(string='Jumlah Indikator', readonly=True, default=44)
    skor_maksimum = fields.Float(string='Skor Maksimum', compute="_compute_skor_maksimum")
    jumlah_skor = fields.Float(string='Jumlah Skor', compute="_compute_jumlah_skor")
    nilai_kinerja = fields.Float(string='Nilai Kinerja', compute="_compute_nilai_kinerja")
    
    
    @api.depends('jumlah_indikator')
    def _compute_skor_maksimum(self):
        for rec in self:
            rec.skor_maksimum = rec.jumlah_indikator * 2

    
    @api.depends('nilai_total_karakteristik_peserta_didik','nilai_total_teori_belajar_dan_prinsip_pembelajaran_yg_mendidik','nilai_total_pengembangan_kurikulum','nilai_total_guru_bertindak_sesuai_norma_agama','nilai_total_guru_menunjukan_pribadi_dewasa_dan_teladan')
    def _compute_jumlah_skor(self):
        for rec in self:
            rec.jumlah_skor = rec.nilai_total_karakteristik_peserta_didik + rec.nilai_total_teori_belajar_dan_prinsip_pembelajaran_yg_mendidik + rec.nilai_total_pengembangan_kurikulum + rec.nilai_total_guru_bertindak_sesuai_norma_agama + rec.nilai_total_guru_menunjukan_pribadi_dewasa_dan_teladan

    @api.depends('jumlah_indikator','skor_maksimum','jumlah_skor')
    def _compute_nilai_kinerja(self):
        for rec in self:
            rec.nilai_kinerja= (rec.jumlah_skor / rec.skor_maksimum) * 100

    # field buat pembagi
    pembagi = fields.Float(string='Pembagi', default=1, readonly=True)
    
    