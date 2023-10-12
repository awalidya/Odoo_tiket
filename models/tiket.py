from odoo import api, fields, models, _

class TiketPesawat(models.Model):
    _name = "tiket.pesawat"
    _description = "pembelian tiket pesawat antar daerah/kota se-provinsi Jawa Timur"
    
    id_tiket = fields.Char(string='Id Tiket')
    name = fields.Char(string= 'Nama', required=True)
    reference = fields.Char(string= 'Order Preference', required=True, copy=False, readonly=True, 
                            default=lambda self: _('New')) 
    tanggal = fields.Date(string='Tanggal')
    maskapai = fields.Text(string='Maskapai')
    kode =fields.Char(string='Kode')
    kota_keberangkatan = fields.Selection([
        ('banyuwangi', 'Banyuwangi'),
        ('gresik', 'Gresik'),
        ('kediri', 'Kediri'),
        ('madura', 'Madura'),
        ('malang', 'Malang'),
        ('surabaya', 'Surabaya')
    ],  required=True, default='banyuwangi')
    kota_tujuan = fields.Selection([
        ('banyuwangi', 'Banyuwangi'),
        ('gresik', 'Gresik'),
        ('kediri', 'Kediri'),
        ('madura', 'Madura'),
        ('malang', 'Malang'),
        ('surabaya', 'Surabaya')
    ],  required=True, default='banyuwangi')   
    age = fields.Integer(string= 'Umur')
    gender = fields.Selection([
        ('male', 'Laki-laki'),
        ('female', 'Perempuan'), 
        ('other', 'Lainnya'),
    ],  required=True, default='male')
    kelas_penerbangan = fields.Selection([
        ('economy', 'Economy'),
        ('business', 'Business'),
        ('first_class', 'First_Class')
    ],  required=True, default='economy')  
    kursi = fields.Selection([
        ('a1', 'A1'),
        ('a2', 'A2'),
        ('a3', 'A3'),
        ('a4', 'A4'),
        ('a5', 'A5'),
        ('b1', 'B1'),
        ('b2', 'B2'),
        ('b3', 'B3'),
        ('b4', 'B4'),
        ('b5', 'B5')
    ],  required=True, default='a1')
    note = fields.Text(string='Catatan')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Canceled')], default='draft', string="Status")
    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Ticket'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('tiket.pesawat') or _('New')
        res = super(TiketPesawat, self).create(vals)
        return res

    @api.onchange('kota_tujuan')
    def get_output(self, kota_tujuan):
        valid_kota=['Banyuwangi', 'Gresik']
        if kota_tujuan in valid_kota:
            if kota_tujuan == 'Banyuwangi':
                kode = 'a'
                return self.kode
        else :
            return 'tdk ada'