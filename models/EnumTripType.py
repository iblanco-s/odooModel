from odoo import models, fields

class TripType(models.Model):
    _name = 'trandom.trip_type'
    _description = 'Trip Type Enumeration'

    CULTURE = 'culture'
    NATURE = 'nature'
    LEISURE = 'leisure'
    SPORTS = 'sports'