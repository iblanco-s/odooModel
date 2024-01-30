from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Trip(models.Model):
    _name = 'trandom.trip'
    _description = 'Trip Entity'

    id = fields.Integer(string='ID')
    trip_type = fields.Selection([('culture', 'Culture'), ('leisure', 'Leisure'), ('nature', 'Nature'),('sports','Sports')], string="Type")
    description = fields.Char(string='Description')
    customer = fields.Many2many('trandom.customer', string='Customer')
    excursions = fields.One2many('trandom.excursions', 'id', string='Excursions')

    @api.constrains('description')
    def _check_description(self):
        for record in self:
            if record.description is False:
                raise ValidationError("La descripcion no puede estar vacía.")
            if not 2 <= len(record.description) <= 200:
                raise ValidationError("La descripción debe tener entre 2 y 200 caracteres")

    @api.constrains('trip_type')
    def _check_trip_type(self):
        for record in self:
            if not record.trip_type:
                raise ValidationError("El tipo de viaje es obligatorio y no puede ser nulo o vacío")

    @api.onchange('trip_type')
    def _onchange_trip_type(self):
        if self.trip_type == 'culture':
            self.description = 'Cultural trip to famous cities (example)'
        elif self.trip_type == 'leisure':
            self.description = 'Leisure trip to relaxing destinations (example)'
        elif self.trip_type == 'nature':
            self.description = 'Nature trip to beautiful landscapes (example)'
        elif self.trip_type == 'sports':
            self.description = 'Sports trip to exciting games (example)'
    @api.model
    def create(self, vals):
        if not isinstance(vals.get('description'), bool):
            vals['description'] = vals.get('description', '').upper()
        return super(Trip, self).create(vals)