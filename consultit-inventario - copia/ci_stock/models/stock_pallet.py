# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class StockPallet(models.Model):
    _name = 'stock.pallet'
    _description = 'Tarima'
    _rec_name = 'nro_tarima'

    nro_tarima = fields.Char('Nro. Tarima')
    container_id = fields.Many2one('stock.container', 'Contenedor')
    pallet_select_ids = fields.Many2many('stock.pallet.select', string='pallet_select')