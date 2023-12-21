# user.py
from odoo import models, fields, api
# from .user_type import UserType

class User(models.Model):
    _name = 'trandom.user'
    _description = 'User'

    mail = fields.Char(string='Mail', required=True)
    password = fields.Char(string='Password', required=True)
    # user_type = fields.Selection(UserType.name, string='User Type', required=True)
