# customer.py
from odoo import models, fields

class Customer(models.Model):
    _inherit = 'trandom.user'
    _name = 'trandom.customer'
    _description = 'Customer'

    name = fields.Char(string='Name')
    surname = fields.Char(string='Surname')
    mail = fields.Char(string='Mail')
    trips = fields.Many2many('trandom.trip', string='Trip')



