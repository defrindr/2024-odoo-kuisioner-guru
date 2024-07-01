from odoo import _, api, fields, models
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
from odoo.exceptions import UserError, ValidationError






class DataGuru(models.Model):
    _name = 'data.guru'
    _description = 'Model untuk tabel data guru'

    name = fields.Char(string='Nama Guru', required=True)
    nuptk = fields.Char(string='NUPTK')
    jenis_kelamin = fields.Selection(string='Jenis Kelamin', selection=[('lk', 'Laki-laki'), ('pr', 'Perempuan')])
    tempat_lahir = fields.Char(string='Tempat Lahir')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    nip = fields.Char(string='NIP')
    status_kepegawaian = fields.Selection(string='Status Kepegawaian', selection=[('pns', 'PNS'),('pppk','PPPK'),('ths', 'Tenaga Honor Sekolah')])
    jenis_ptk = fields.Char(string='Jenis PTK')
    agama = fields.Selection(string='Agama', selection=[('islam', 'Islam'), ('kristen', 'Kristen'),('katolik', 'Katolik'), ('hindu', 'Hindu'),('budha', 'Budha'), ('konghucu', 'Konghucu'),('lain-lain','Lain-lain')])
    alamat_jalan = fields.Char(string='Alamat Jalan')
    rt = fields.Integer(string='RT')
    rw = fields.Integer(string='RW')
    nama_dusun = fields.Char(string='Nama Dusun')
    desa_kelurahan = fields.Char(string='Desa/Kelurahan')
    kecamatan = fields.Char(string='Kecamatan')
    kode_pos = fields.Integer(string='Kode Pos')
    telefon = fields.Char(string='Telepon')
    email = fields.Char(string='E-mail')
    tugas_tambahan = fields.Char(string='Tugas Tambahan')
    # DATA SUDAH PNS jika data status kepegawaian adalah pns
    pns = fields.Boolean(string='PNS', compute="_compute_pns")
    sk_cpns = fields.Char(string='SK CPNS / PPPK')
    tgl_cpns = fields.Date(string='Tanggal CPNS / PPPK')
    sk_pengangkatan = fields.Char(string='SK Pengangkatan')
    tmt_pengangkatan = fields.Date(string='TMT Pengangkatan')
    lembaga_pengangkatan = fields.Char(string='Lembaga Pengangkatan')
    pangkat_golongan = fields.Char(string='Pangkat Golongan')
    
    nama_ibu_kandung = fields.Char(string='Nama Ibu Kandung')
    # DATA STATUS PERKAWINAN
    status_perkawinan = fields.Selection(string='Status Perkawinan', selection=[('kawin', 'Kawin'), ('tidak kawin', 'Belum Kawin')], default="tidak kawin")
    nama_suami_istri = fields.Char(string='Nama Suami/Istri')
    
    npwp = fields.Char(string='NPWP')
    nik = fields.Char(string='NIK')
    no_kk = fields.Char(string='No.KK')
    
    foto = fields.Binary(string='Foto Guru')

    
    # Menambahkan SQL constraint
    _sql_constraints = [
        ('unique_nik', 'UNIQUE(nik)', 'Data guru ini telah tersedia!')
    ]

    @api.depends('status_kepegawaian')
    def _compute_pns(self):
        for rec in self:
            if rec.status_kepegawaian == 'pns' or rec.status_kepegawaian == 'pppk':
                rec.pns = True
            else:
                rec.pns = False  
 
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
