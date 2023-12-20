from odoo import models, fields

class TripInfoId(models.Model):
    _name = 'trandom.trip_info_id'
    _description = 'Trip Information ID'

    trip_id = fields.Integer(string='Trip ID')
    customer_id = fields.Char(string='Customer ID')
