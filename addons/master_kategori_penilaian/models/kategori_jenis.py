from odoo import fields, models, api

class KategoriJenis(models.Model):
    _name = 'kategori.jenis'
    _description = 'Model untuk tabel kategori jenis'
    
    jenis = fields.Char(
        string="Jenis Penilaian",
        required=True
    )
    group_id = fields.Many2one('kategori.group', string='Kategori Group', ondelete='cascade')
    keterangan_ids = fields.One2many('kategori.keterangan', 'jenis_id', string='Detail')

