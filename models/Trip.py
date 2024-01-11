from odoo import models, fields

class Trip(models.Model):
    _name = 'trandom.trip'
    _description = 'Trip Entity'

    id = fields.Integer(string='ID')
    trip_type = fields.Selection([('culture', 'Culture'), ('leisure', 'Leisure'), ('nature', 'Nature'),('sports','Sports')], string="Type")
    description = fields.Char(string='Description')
    trip_info = fields.One2many('trandom.trip_info', 'trip_id', string='Trip Info')
