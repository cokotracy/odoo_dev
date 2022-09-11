# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class StockContainer(models.Model):
    _name = 'stock.container'
    _description = 'Información del Contenedor'
    _rec_name = 'nro_container'

    nro_container = fields.Char('Nro. Contenedor')
    nro_control = fields.Char('Nro. Control')
    partner_id = fields.Many2one('res.partner', 'Propietario')
    cod_partner = fields.Char('Código Propietario')
    dua_id = fields.Many2one('stock.dua', 'Nro. DUA')
    pallet_ids = fields.One2many('stock.pallet', 'container_id', 'Tarimas')
    

    