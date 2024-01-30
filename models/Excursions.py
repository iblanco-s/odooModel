from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class Excursions(models.Model):
    _name = 'trandom.excursions'
    _description = 'Trandom entity'

    name = fields.Char(string='Name')
    date = fields.Date(string='Date')
    duration = fields.Integer(string='Duration')
    trip_id = fields.Many2one('trandom.trip', string='Trip')

    @api.constrains('name')
    def _check_name(self):
        for record in self:
            if record.name is False:
                raise ValidationError("El nombre no puede estar vacío.")
            if not 1 <= len(record.name) <= 50:
                raise ValidationError("El nombre debe tener entre 1 y 50 caracteres.")

    @api.constrains('date')
    def _check_date(self):
        for record in self:
            if record.date is False:
                raise ValidationError("La fecha no puede estar vacía.")
            if record.date < date.today():
                raise ValidationError("La fecha debe ser futura y no puede ser pasada.")

    @api.constrains('duration')
    def _check_duration(self):
        for record in self:
            if record.duration is False:
                raise ValidationError("La duracion no puede estar vacía.")
            if not 1 <= record.duration <= 9999:
                raise ValidationError("La duración debe ser un número positivo y no puede exceder 9999.")