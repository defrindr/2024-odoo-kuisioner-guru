from odoo import _, api, fields, models
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
from odoo.exceptions import ValidationError




class DataABsensiKehadiran(models.Model):
    _name = 'absensi.kehadiran'
    _description = 'Model untuk tabel data absensi kehadiran'

    name = fields.Date(string='Tanggal Absensi',default=datetime.now(), required=True)
    nama_guru = fields.Many2one(comodel_name='data.guru', string='Nama Guru', required=True, ondelete='cascade')
    kehadiran = fields.Selection(string='Kehadiran', selection=[('hadir', 'Hadir'), ('tidak hadir', 'Tidak Hadir')], required=True)
    check_in = fields.Float(string='Check-in')
    check_out = fields.Float(string='Check-out')
    terlambat = fields.Float(string='Terlambat (Menit)', default=0.0, compute="_compute_terlambat")
    keterangan = fields.Selection(string='Keterangan', selection=[('sakit', 'Sakit'), ('izin', 'Izin'),('alpha','Alpha')])
    is_invisible = fields.Boolean(string='', compute="_compute_is_invisible")
    

    @api.depends('kehadiran')
    def _compute_is_invisible(self):
        for rec in self:
            if rec.kehadiran == 'hadir':
                rec.is_invisible = True
            else:
                rec.is_invisible = False    


    @api.constrains('check_in')
    def _check_check_in(self):
        for rec in self:
            if rec.check_in >= 23.99 or rec.check_in < 0.0:
                raise ValidationError("Hanya bisa mengisikan Check in antara pukul 00.00 - 23.59")
    
    @api.constrains('check_out')
    def _check_check_out(self):
        for rec in self:
            if rec.check_out >= 23.99 or rec.check_out < 0.0:
                raise ValidationError("Hanya bisa mengisikan Check Out antara pukul 00.00 - 23.59")
                # if rec.check_out <= rec.check_in:
                #     raise ValidationError("waktu Check out tidak boleh kurang dari nilai waktu check in")

    
    @api.onchange('kehadiran')
    def _onchange_check_in_check_out(self):
        for rec in self:
            if rec.kehadiran == 'tidak hadir':
                rec.check_in = 0.0
                rec.check_out = 0.0


    @api.depends('check_in','check_out')
    def _compute_terlambat(self):
        for rec in self:
            if rec.check_in <= 7.0:
                rec.terlambat = 0.0
            else:
                rec.terlambat = rec.check_in - 7.0

    


            
    
    
    
    
    
    
        
