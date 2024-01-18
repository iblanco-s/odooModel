from odoo import models, fields

class Excursions(models.Model):
    _name = 'trandom.excursions'
    _description = 'Trandom entity'

    name = fields.Char(string='Name')
    date = fields.Date(string='Date')
    duration = fields.Integer(string= 'Duration')
    trip_id = fields.Many2one('trandom.trip', string='Trip')