# customer.py
from odoo import models, fields

class Customer(models.Model):
    _inherit = 'trandom.user'
    _name = 'trandom.customer'
    _description = 'Customer'

    name = fields.Char(string='Name', required=True)
    zip = fields.Integer(string='Zip')
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
