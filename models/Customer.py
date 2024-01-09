# customer.py
from odoo import models, fields

class Customer(models.Model):
    _inherit = 'res.users'
    #_name = 'trandom.customer'
    _description = 'Customer'

    trip_infos = fields.One2many('trandom.trip_info', 'customer_id',  String='Trip Infos')


