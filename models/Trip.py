from odoo import models, fields

class Trip(models.Model):
    _name = 'trandom.trip'
    _description = 'Trip Entity'

    id = fields.Integer(string='ID')
    trip_type = fields.Many2one('trandom.trip_type', string='Trip Type')
    trip_info_ids = fields.One2many('trandom.trip_info', 'trip_info_id', string='Trip Info')
    description = fields.Char(string='Description')
