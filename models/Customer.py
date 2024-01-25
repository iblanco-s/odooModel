from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class Customer(models.Model):
    _inherit = 'trandom.user'
    _name = 'trandom.customer'
    _description = 'Customer'

    name = fields.Char(string='Name')
    surname = fields.Char(string='Surname')
    mail = fields.Char(string='Mail')
    trips = fields.Many2many('trandom.trip', string='Trip')

    @api.constrains('mail')
    def _check_mail_format(self):
        for record in self:
            if record.mail and not record.mail.endswith('@gmail.com'):
                raise ValidationError("The mail has to end with '@gmail.com'")

    @api.constrains('name')
    def _check_name(self):
        for record in self:
            if not record.name:
                raise ValidationError("The Name can't be empty")

    @api.constrains('surname')
    def _check_surname(self):
        for record in self:
            if not record.surname:
                raise ValidationError("The Name can't be empty")

    @api.onchange('name', 'surname')
    def _onchange_name_and_surname_no_numbers(self):
        for record in self:
            if record.name:
                if any(char.isdigit() for char in record.name):
                    raise ValidationError("The name can't have numbers on it")
            if record.surname:
                if any(char.isdigit() for char in record.surname):
                    raise ValidationError("The surname can't have numbers on it")


    @api.model
    def create(self, vals):
        if 'name' in vals and vals['name']:
            vals['name'] = vals['name'].capitalize()
        if 'surname' in vals and vals['surname']:
            vals['surname'] = vals['surname'].capitalize()

        return super(Customer, self).create(vals)