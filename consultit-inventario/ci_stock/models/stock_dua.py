# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class StockDUA(models.Model):
    _name = 'stock.dua'
    _description = 'DUA'
    _rec_name = 'nro_dua'

    nro_dua = fields.Char('Nro. DUA')
    reg_date = fields.Date('Fecha registro')
    nro_envio = fields.Char('Nro. Envío')
    mov_tica = fields.Char('Movimiento TICA')
    container_id = fields.Many2one('stock.fleet.container', 'Nro. Contenedor')