from odoo import fields, models, api

class KategoriGroup(models.Model):
    _name = 'kategori.group'
    _description = 'Model untuk tabel kategori group'
    
    name = fields.Char(string="Nama Group", compute="_compute_name", store=True)
    kategori = fields.Selection(
        string="Grup Kategori",
        selection=[
            ('kepala_sekolah', 'Form Penilaian Kepala Sekolah'),
            ('teman_sejawat', 'Form Penilaian Teman Sejawat'),
            ('wali_murid', 'Form Penilaian Wali Murid'),
            ('peserta_didik', 'Form Penilaian Peserta Didik'),
        ],
        required=True
    )

    
    @api.depends("kategori")
    def _compute_name(self):
        for rec in self:
            data_kategori = {
                'kepala_sekolah': 'Form Penilaian Kepala Sekolah',
                'teman_sejawat':'Form Penilaian Teman Sejawat',
                'wali_murid':'Form Penilaian Wali Murid',
                'peserta_didik':'Form Penilaian Peserta Didik',
            }
            rec.name = data_kategori[rec.kategori]

    jenis_ids = fields.One2many('kategori.jenis', 'group_id', string='Kategori Jenis')

    
    # Menambahkan SQL constraint
    _sql_constraints = [
        ('unique_kategori', 'UNIQUE(kategori)', 'Data kategori ini telah tersedia!')
    ]


    def confirm(self):
        # Perform any required logic here

        # Redirect to another page or action
        return {
            'type': 'ir.actions.act_url',
            'url': '/my/custom/page',  # Replace with your desired URL or action
            'target': 'self',  # Open in the same window/tab
        }