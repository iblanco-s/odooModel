# user_type.py
from odoo import models, fields

class UserType(models.Model):
    _name = 'trandom.user_type'
    _description = 'User Type'

    name = fields.Selection([('admin', 'Admin'), ('customer', 'Customer')],
                            string='User Type', required=True)
