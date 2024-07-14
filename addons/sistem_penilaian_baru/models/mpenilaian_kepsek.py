from odoo import models,fields,api
from datetime import date, datetime
import random
from odoo.exceptions import ValidationError

import logging

_logger = logging.getLogger(__name__)
class MpenilaianKepsek(models.Model):
    _name="mpenilaian.kepsek"
    _description="Model untuk Penialaian Kepsek"
    
    tanggal = fields.Date(string='Tanggal Penilaian', default=datetime.now(), required=True)
    nama_responden = fields.Char(string='Nama Responden', required="True", default=lambda self: self.env.user.name)
    jabatan = fields.Selection(string='Jabatan', selection="_get_dynamic_group_selection")

    # Belongs To
    data_guru_id = fields.Many2one(comodel_name='data.guru', string='Guru yang di nilai', required="True", ondelete="cascade")
    group_id = fields.Many2one(
        comodel_name='kategori.group', 
        string='Group', 
        required="True", 
        ondelete="cascade",
        compute="_computed_group_id",
        store=True
    )
    # Has Relations
    penilaian_kepsek_detail_ids = fields.One2many('mpenilaian.kepsek.detail', 'penilaian_id', string='Detail Pertanyaan')
    
    status = fields.Selection(string="Status Pengisian", selection=[('pending', 'Pending'), ('selesai', 'Selesai')], default='pending', readonly=1)
    total_nilai = fields.Integer(string="Total Nilai", default=0, readonly=1)
    
    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, f"{rec.tanggal} - {rec.data_guru_id.name}"))
        return result
    

    def _get_dynamic_group_selection(self):
        user = self.env.user
        groups = []

        if user.has_group('sistem_penilaian_baru.group_admin_kinerja_guru_baru'):
            groups.append(('Kepala Sekolah', 'Kepala Sekolah'))
            groups.append(('Wali Murid', 'Wali Murid'))
            groups.append(('Guru', 'Guru'))
            groups.append(('Peserta Didik', 'peserta Didik'))
        if user.has_group('sistem_penilaian_baru.group_kepsek_baru'):
            groups.append(('Kepala Sekolah', 'Kepala Sekolah'))
        if user.has_group('sistem_penilaian_baru.group_wali_murit_baru'):
            groups.append(('Wali Murid', 'Wali Murid'))
        if user.has_group('sistem_penilaian_baru.group_teman_sejawat_baru'):
            groups.append(('Guru', 'Guru'))
        if user.has_group('sistem_penilaian_baru.group_peserta_didik_baru'):
            groups.append(('Peserta Didik', 'peserta Didik'))
        # Add other groups as needed

        _logger.info('list group')
        _logger.info(groups)

        return groups


    # Functions

    @api.depends('jabatan')
    def _computed_group_id(self):
        model_kategori_group = self.env['kategori.group']
        _logger.info('jabatanselect')
        for rec in self:
            _logger.info(rec.jabatan)
            if rec.jabatan == "Kepala Sekolah":
                q = "kepala_sekolah"
            elif rec.jabatan == "Guru":
                q = "teman_sejawat"
            elif rec.jabatan == "Wali Murid":
                q = "wali_murid"
            elif rec.jabatan == "Peserta Didik":
                q = "peserta_didik"
            else:
                q = "bayi_macan"
            print(f'jabatan: {q}')
            data = model_kategori_group.search([('kategori', '=', q)])
            if data:
                rec.group_id = data.id
            else:
                rec.group_id = False



    @api.model
    def default_get(self, fields):
        res = super(MpenilaianKepsek, self).default_get(fields)
        # selection = self._get_dynamic_group_selection()
        _logger.info('from selection')
        # if selection:
        #     res['group_selection'] = selection[0][0]  # Default to the first option
        return res

    @api.model
    def create(self, vals):
        _logger.info('rec start')
        model_kategori_group = self.env['kategori.group']
        if vals['jabatan'] == "Kepala Sekolah":
            q = "kepala_sekolah"
        elif vals['jabatan'] == "Guru":
            q = "teman_sejawat"
        elif vals['jabatan'] == "Wali Murid":
            q = "wali_murid"
        elif vals['jabatan'] == "Peserta Didik":
            q = "peserta_didik"
        else:
            q = "bayi_macan"
        data = model_kategori_group.search([('kategori', '=', q)])
        if data:
            vals['group_id'] = data.id
        else:
            vals['group_id'] = False

        if 'group_id' not in vals.keys() or vals['group_id'] == None or vals['group_id'] == False:
            raise ValidationError('Harap pilih jabatan terlebih dulu')

        exist = self.search_count([('data_guru_id', '=', vals['data_guru_id']),
                         ('group_id', '=', vals['group_id']),
                         ('create_uid', '=', self.env.user.id)])
        if exist != 0:
            raise ValidationError('Data sudah ada')
        record = super(MpenilaianKepsek, self).create(vals)
        record._populate_options()
        record._check_penilaian_kepsek_detail_ids()
        # Redirect to form view after creation
        _logger.info(f'Id nya adalah {record.id}')
        return record
    
    @api.constrains('penilaian_kepsek_detail_ids')
    def _check_penilaian_kepsek_detail_ids(self):
        for record in self:
          detail_model = self.env['mpenilaian.kepsek.detail']
          data_nilai_none = detail_model.search_count([('penilaian_id', '=', self.id), ('nilai', '=', False)])
          _logger.info('data_nilai_none')
          _logger.info(data_nilai_none)
          if data_nilai_none == 0:
              data_detail = detail_model.search([('penilaian_id', '=', self.id)])
              jumlah_item = len(data_detail)
              maksimum_nilai = jumlah_item * 2
              jumlah_nilai = 0
              for item in data_detail:
                  if item.nilai == "sering":
                      jumlah_nilai += 2
                  elif item.nilai == "kadang_kadang":
                      jumlah_nilai += 1
              if maksimum_nilai != 0 and jumlah_nilai != 0:
                  self.total_nilai = (jumlah_nilai / maksimum_nilai) * 100
                  self.status = 'selesai'
              _logger.info('Nilai telah diatur')
          else:
              self.status = 'pending'
              self.total_nilai = 0 
              pass
    def _populate_options(self):
        detail_model = self.env['mpenilaian.kepsek.detail']
        existing_characteristics = detail_model.search([('penilaian_id', '=', self.id)])
        if not existing_characteristics:
            keterangan_model = self.env['kategori.keterangan']
            keterangan_list = keterangan_model.search([('group_id', '=', self.group_id.id)])
            for index, item in enumerate(keterangan_list):
                data = {
                    'penilaian_id': self.id,
                    'jenis_id': item.jenis_id.id,
                    'keterangan_id': item.id,
                    'nilai': 'sering'
                    # 'nilai': random.choices(['sering', 'kadang_kadang', 'tidak_pernah'])[0]
                }
                _logger.info(data)
                detail_model.create(data)