# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class StockFleetContainer(models.Model):
    _name = 'stock.fleet.container'
    _description = 'Container'
    _rec_name = 'container_number'

    base_container_number = fields.Char('Nro. contenedor base')
    nro_control = fields.Char('Nro. control')
    container_number = fields.Char(compute="compute_display_container_number", store=True, string='Nro. contenedor impreso')
    vehicle_id = fields.Many2one('fleet.vehicle', 'Vehículo')
    dua_ids = fields.One2many('stock.dua', 'container_id', string='DUA')

    @api.depends('base_container_number', 'nro_control')
    def compute_display_container_number(self):
        if self.base_container_number or self.nro_control:
            self.container_number = str(self.base_container_number) + ' ' + str(self.nro_control)
        return self.container_number



