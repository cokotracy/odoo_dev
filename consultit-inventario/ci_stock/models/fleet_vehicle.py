# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    container_ids = fields.One2many('stock.fleet.container', 'vehicle_id', string='Contenedor')