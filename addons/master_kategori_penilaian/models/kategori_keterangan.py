from odoo import fields, models, api

class KategoriKeterangan(models.Model):
    _name = 'kategori.keterangan'
    _description = 'Model untuk tabel kategori keterangan'
    
    keterangan = fields.Char(
        string="Keterangan"
    )
    jenis_id = fields.Many2one('kategori.jenis', string='Jenis', ondelete='cascade')
    group_id = fields.Many2one('kategori.group', string='Grup', ondelete='cascade')

    @api.onchange('keterangan')
    def _compute_group_id(self):
        for rec in self:
            rec.group_id = rec.jenis_id.group_id

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, rec.keterangan))
        return result
