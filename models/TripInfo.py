from odoo import models, fields, api

class TripInfo(models.Model):
    _name = 'trandom.trip_info'
    _description = 'Trip Information'

    trip_info_id = fields.Many2one('trandom.trip_info_id', string='Trip Information ID')
    initial_date = fields.Date(string='Initial Date')
    last_date = fields.Date(string='Last Date')
    trip_id = fields.Many2one('trandom.trip', string='Trip')
    customer_id = fields.Many2one('trandom.customer', string='Customer')
