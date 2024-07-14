from datetime import datetime
from odoo import models, fields, api

class Mnilai_total(models.Model):
    _name="mnilai.total"
    _deksripsi="Report untuk Akumulasi dari penilaian guru"

    guru_id = fields.Many2one(comodel_name='data.guru', string='Guru yang di nilai', required="True", ondelete="cascade")    
    tanggal = fields.Date(string='Tanggal Penerbitan', default=datetime.now())
    data_kepala_sekolah_id = fields.Many2one(comodel_name='res.users', string='Nama Kepala Sekolah', ondelete="cascade", compute="_compute_kepala_sekolah", store=True)

    nilai_kepala_sekolah = fields.Float(string='Nilai dari kepala sekolah', compute='_compute_total_nilai', store=True)
    nilai_wali_murid = fields.Float(string='Nilai dari Wali Murid', compute='_compute_total_nilai', store=True)
    nilai_teman_sejawat = fields.Float(string='Nilai dari Teman sejawat', compute='_compute_total_nilai', store=True)
    nilai_peserta_didik = fields.Float(string='Nilai dari Peserta Didik', compute='_compute_total_nilai', store=True)

    bobot_nilai_kepala_sekolah = fields.Float(string='Bobot nilai dari kepala sekolah', compute='_compute_total_nilai', store=True)
    bobot_nilai_wali_murid = fields.Float(string='Bobot nilai dari Wali Murid', compute='_compute_total_nilai', store=True)
    bobot_nilai_teman_sejawat = fields.Float(string='Bobot nilai dari Teman sejawat', compute='_compute_total_nilai', store=True)
    bobot_nilai_peserta_didik = fields.Float(string='Bobot nilai dari Peserta Didik', compute='_compute_total_nilai', store=True)

    total_nilai_kepala_sekolah = fields.Float(string='Total nilai dari kepala sekolah', compute='_compute_total_nilai', store=True)
    total_nilai_wali_murid = fields.Float(string='Total nilai dari Wali Murid', compute='_compute_total_nilai', store=True)
    total_nilai_teman_sejawat = fields.Float(string='Total nilai dari Teman sejawat', compute='_compute_total_nilai', store=True)
    total_nilai_peserta_didik = fields.Float(string='Total nilai dari Peserta Didik', compute='_compute_total_nilai', store=True)

    total_nilai = fields.Float(string='Total Nilai', compute='_compute_total_nilai', store=True)

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, f"{rec.tanggal} - {rec.guru_id.name}"))
        return result


    @api.depends('guru_id')
    def _compute_kepala_sekolah(self):
        for rec in self:
            # Retrieve users belonging to a specific group ID
            group = self.env['res.groups'].search([('name', '=', 'Access Penilaian Kepala Sekolah (Baru)')])
            rec.data_kepala_sekolah_id=1
            if group:
                users = group.users
                if users:
                    rec.data_kepala_sekolah_id = users[0].id
                else:
                    rec.data_kepala_sekolah_id = -1
            else:
                rec.data_kepala_sekolah_id = 0  

    @api.depends('guru_id')
    def _compute_total_nilai(self):
        model_penilaian = self.env['mpenilaian.kepsek']
        model_group = self.env['kategori.group']
        for rec in self:
             tanggalAwal = ('tanggal', '>=', datetime(rec.tanggal.year, 1, 1))
             tanggalAkhir = ('tanggal', '<=', datetime(rec.tanggal.year, 12, 31))
            #  ------------------
             kg = model_group.search([('kategori', '=', 'kepala_sekolah')], limit=1)
             total_nilai_kepala_sekolah = 0
             total_kepala_sekolah = 0
             bobot_kepala_sekolah = 0
             nks = model_penilaian.search([('data_guru_id', '=', rec.guru_id.id), ('group_id', '=', kg.id), tanggalAwal, tanggalAkhir])
             for n in nks:
                 total_kepala_sekolah += 1
                 total_nilai_kepala_sekolah += n.total_nilai
                 bobot_kepala_sekolah = n.group_id.bobot
             # Cari rata rata nilai  
             if total_kepala_sekolah > 0:
                 total_nilai_kepala_sekolah = total_nilai_kepala_sekolah / total_kepala_sekolah
             #  Fill column
             if nks:
                 rec.nilai_kepala_sekolah = total_nilai_kepala_sekolah
                 rec.bobot_nilai_kepala_sekolah = bobot_kepala_sekolah
                 rec.total_nilai_kepala_sekolah = total_nilai_kepala_sekolah*(bobot_kepala_sekolah / 100)
             else:
                 rec.nilai_kepala_sekolah = 0
                 rec.bobot_nilai_kepala_sekolah = 0
                 rec.total_nilai_kepala_sekolah = 0
            #  ------------------
             tsg = model_group.search([('kategori', '=', 'teman_sejawat')], limit=1)
             total_nilai_teman_sejawat = 0
             total_teman_sejawat = 0
             bobot_teman_sejawat = 0
             nts = model_penilaian.search([('data_guru_id', '=', rec.guru_id.id), ('group_id', '=', tsg.id), tanggalAwal, tanggalAkhir])
             for n in nts:
                 total_teman_sejawat += 1
                 total_nilai_teman_sejawat += n.total_nilai
                 bobot_teman_sejawat = n.group_id.bobot
             # Cari rata rata nilai  
             if total_teman_sejawat > 0:
                 total_nilai_teman_sejawat = total_nilai_teman_sejawat / total_teman_sejawat
             #  Fill column
             if nts:
                 rec.nilai_teman_sejawat = total_nilai_teman_sejawat
                 rec.bobot_nilai_teman_sejawat = bobot_teman_sejawat
                 rec.total_nilai_teman_sejawat = total_nilai_teman_sejawat*(bobot_teman_sejawat / 100)
             else:
                 rec.nilai_teman_sejawat = 0
                 rec.bobot_nilai_teman_sejawat = 0
                 rec.total_nilai_teman_sejawat = 0
            #  ------------------
             wmg = model_group.search([('kategori', '=', 'wali_murid')], limit=1)
             total_nilai_wali_murid = 0
             total_wali_murid = 0
             bobot_wali_murid = 0
             nwm = model_penilaian.search([('data_guru_id', '=', rec.guru_id.id), ('group_id', '=', wmg.id), tanggalAwal, tanggalAkhir])
             for n in nwm:
                 total_wali_murid += 1
                 total_nilai_wali_murid += n.total_nilai
                 bobot_wali_murid = n.group_id.bobot
             # Cari rata rata nilai  
             if total_wali_murid > 0:
                 total_nilai_wali_murid = total_nilai_wali_murid / total_wali_murid
             #  Fill column
             if nwm:
                 rec.nilai_wali_murid = total_nilai_wali_murid
                 rec.bobot_nilai_wali_murid = bobot_wali_murid
                 rec.total_nilai_wali_murid = total_nilai_wali_murid*(bobot_wali_murid / 100)
             else:
                 rec.nilai_wali_murid = 0
                 rec.bobot_nilai_wali_murid = 0
                 rec.total_nilai_wali_murid = 0
            #  ------------------
             pdg = model_group.search([('kategori', '=', 'peserta_didik')], limit=1)
             total_nilai_peserta_didik = 0
             total_peserta_didik = 0
             bobot_peserta_didik = 0
             npd = model_penilaian.search([('data_guru_id', '=', rec.guru_id.id), ('group_id', '=', pdg.id), tanggalAwal, tanggalAkhir])
             for n in npd:
                 total_peserta_didik += 1
                 total_nilai_peserta_didik += n.total_nilai
                 bobot_peserta_didik = n.group_id.bobot
             # Cari rata rata nilai  
             if total_peserta_didik > 0:
                 total_nilai_peserta_didik = total_nilai_peserta_didik / total_peserta_didik
             #  Fill column
             if npd:
                 rec.nilai_peserta_didik = total_nilai_peserta_didik
                 rec.bobot_nilai_peserta_didik = bobot_peserta_didik
                 rec.total_nilai_peserta_didik = total_nilai_peserta_didik*(bobot_peserta_didik / 100)
             else:
                 rec.nilai_peserta_didik = 0
                 rec.bobot_nilai_peserta_didik = 0
                 rec.total_nilai_peserta_didik = 0
             rec.total_nilai = rec.total_nilai_kepala_sekolah+rec.total_nilai_teman_sejawat+rec.total_nilai_wali_murid+rec.total_nilai_peserta_didik
                 
