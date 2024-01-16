from odoo import models, fields

class User(models.Model):
    _name = 'trandom.user'
    _description = 'User'

    admin = fields.Boolean()


