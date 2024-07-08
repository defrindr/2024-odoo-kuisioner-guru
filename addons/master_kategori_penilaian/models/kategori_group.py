from odoo import fields, models, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


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
    bobot = fields.Integer(
        string="Bobot Nilai",
        required=True,
        store=True
    )

    sisa_bobot = fields.Integer(string='Sisa Bobot', store=False, default= lambda self: 100 - sum(self.search([]).mapped('bobot')),readonly=True)
    
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


    @api.constrains('bobot')
    def _check_bobot_sum(self):
        for record in self:
            # Calculate the total bobot sum excluding the current record
            total_bobot = sum(self.search([]).mapped('bobot')) - record.bobot
            _logger.info(f"total bobot: {total_bobot}")
            # Add the bobot value of the current record
            if total_bobot + record.bobot > 100:
                raise ValidationError("Sum of Bobot cannot exceed 100.")

    @api.model
    def create(self, vals):
        # Perform additional checks before create
        if 'bobot' in vals:
            total_bobot = sum(self.search([]).mapped('bobot')) + vals['bobot']
            _logger.info(f"total bobot: {total_bobot}")
            if total_bobot > 100:
                raise ValidationError("Sum of Bobot cannot exceed 100.")

        return super(KategoriGroup, self).create(vals)

    def write(self, vals):
        # Perform additional checks before update
        if 'bobot' in vals:
            total_bobot = sum(self.search([]).mapped('bobot')) - self.bobot + vals['bobot']
            _logger.info(f"total bobot: {total_bobot}")
            if total_bobot > 100:
                raise ValidationError("Sum of Bobot cannot exceed 100.")

        return super(KategoriGroup, self).write(vals)
