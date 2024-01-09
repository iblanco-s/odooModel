from odoo import models, fields

class City(models.Model):
    _name = 'trandom.city'
    _description = 'City Entity'

    name = fields.Char(string='Name')
    country = fields.Char(string='Country')
    population = fields.Selection([('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], string="Population")
    weather = fields.Selection([('summer', 'Summer'), ('spring', 'Spring'), ('autumn', 'Autumn'), ('winter', 'Winter')], string="Weather")
    trips = fields.Many2many('trandom.trip', string='Trips')
