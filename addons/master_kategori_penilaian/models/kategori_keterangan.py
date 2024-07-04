from odoo import fields, models

class KategoriKeterangan(models.Model):
    _name = 'kategori.keterangan'
    _description = 'Model untuk tabel kategori keterangan'
    
    keterangan = fields.Char(
        string="Keterangan"
    )
    jenis_id = fields.Many2one('kategori.jenis', string='Jenis', ondelete='cascade')