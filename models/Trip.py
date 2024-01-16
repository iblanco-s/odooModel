from odoo import models, fields

class Trip(models.Model):
    _name = 'trandom.trip'
    _description = 'Trip Entity'

    id = fields.Integer(string='ID')
    trip_type = fields.Selection([('culture', 'Culture'), ('leisure', 'Leisure'), ('nature', 'Nature'),('sports','Sports')], string="Type")
    description = fields.Char(string='Description')
    customer = fields.Many2many('trandom.customer', string='Customer')
    excursions_id = fields.One2many('trandom.excursions', 'id', string='Excursions')
