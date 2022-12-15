# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class FleetVehicleModel(models.Model):
     _inherit = 'fleet.vehicle.model'

     vehicle_type = fields.Selection([
        ('car', 'Car'), 
        ('bike', 'Bike'),
        ('truck', 'Truck')], default='car', required=False)