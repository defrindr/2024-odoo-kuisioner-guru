from odoo import api, fields, models, _
from odoo.exceptions import UserError
import csv
import base64
from io import StringIO
import xlrd
import logging

_logger = logging.getLogger(__name__)


class ImportGuruWizard(models.TransientModel):
    _name = 'import.guru.wizard'
    _description = 'Wizard untuk Impor Data Guru dari CSV'

    file_data = fields.Binary(string="File CSV", required=True)
    file_name = fields.Char(string="Nama File")
    row_index = fields.Integer(string="Nomor Baris", required=True, default=1)

    def import_excel(self):
        if not self.file_data:
            raise UserError(_("Silakan unggah file Excel."))

        if self.row_index < 1:
            raise UserError(_("Nomor baris harus lebih besar dari atau sama dengan 1."))

        # Decode the file data
        data = base64.b64decode(self.file_data)
        workbook = xlrd.open_workbook(file_contents=data)
        sheet = workbook.sheet_by_index(0)

        # Log the contents of the Excel file
        for row_idx in range(sheet.nrows):
            row_values = [sheet.cell_value(row_idx, col) for col in range(sheet.ncols)]
            _logger.info("Baris %s: %s", row_idx, row_values)

        required_fields = ['Nama', 'NUPTK', 'JK', 'Tempat Lahir', 'Tanggal Lahir', 'NIP',
                           'Status Kepegawaian', 'Jenis PTK', 'Agama', 'Alamat Jalan', 'RT', 'RW',
                           'Nama Dusun', 'Desa/Kelurahan', 'Kecamatan', 'Kode Pos', 'Telepon', 'Email',
                           'Tugas Tambahan', 'SK CPNS', 'Tanggal CPNS', 'SK Pengangkatan', 'TMT Pengangkatan',
                           'Lembaga Pengangkatan', 'Pangkat Golongan', 'Nama Ibu Kandung', 'Status Perkawinan',
                           'Nama Suami/Istri', 'NPWP', 'NIK', 'No KK']

        # Check if the Excel file contains the required fields
        header = [sheet.cell_value(0, col) for col in range(sheet.ncols)]
        missing_fields = [field for field in required_fields if field not in header]
        if missing_fields:
            raise UserError(_("File Excel tidak memiliki kolom: %s" % ', '.join(missing_fields)))

        # Get the specific row based on the row index
        row_idx = self.row_index
        if row_idx >= sheet.nrows:
            raise UserError(_("Nomor baris di luar jangkauan. Total baris: %s" % sheet.nrows))

        row = {header[col]: sheet.cell_value(row_idx, col) for col in range(sheet.ncols)}
        self.env['data.guru'].create({
            'name': row['Nama'],
            'nuptk': row['NUPTK'],
            'jenis_kelamin': row['JK'],
            'tempat_lahir': row['Tempat Lahir'],
            'tgl_lahir': row['Tanggal Lahir'] if row['Tanggal Lahir'] else None,
            'nip': row['NIP'],
            'status_kepegawaian': row['Status Kepegawaian'].lower(),
            'jenis_ptk': row['Jenis PTK'],
            'agama': row['Agama'].lower(),
            'alamat_jalan': row['Alamat Jalan'],
            'rt': int(row['RT']) if row['RT'] else None,
            'rw': int(row['RW']) if row['RW'] else None,
            'nama_dusun': row['Nama Dusun'],
            'desa_kelurahan': row['Desa/Kelurahan'],
            'kecamatan': row['Kecamatan'],
            'kode_pos': int(row['Kode Pos']) if row['Kode Pos'] else None,
            'telefon': row['Telepon'],
            'email': row['Email'],
            'tugas_tambahan': row['Tugas Tambahan'],
            'sk_cpns': row['SK CPNS'],
            'tgl_cpns': row['Tanggal CPNS'] if row['Tanggal CPNS']  else None,
            'sk_pengangkatan': row['SK Pengangkatan'],
            'tmt_pengangkatan': row['TMT Pengangkatan'],
            'lembaga_pengangkatan': row['Lembaga Pengangkatan'],
            'pangkat_golongan': row['Pangkat Golongan'],
            'nama_ibu_kandung': row['Nama Ibu Kandung'],
            'status_perkawinan': row['Status Perkawinan'].lower(),
            'nama_suami_istri': row['Nama Suami/Istri'],
            'npwp': row['NPWP'],
            'nik': row['NIK'],
            'no_kk': row['No KK'],
        })

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }