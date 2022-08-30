# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models, _


class StockBatch(models.Model):
    _name = 'stock.batch'
    _description = 'Batch'
    # _rec_name = 'nro_doc'

    cargo_entry_id = fields.Many2one('stock.cargo.entry.control', string='Control de Ingreso de Carga')
    nro_pallet = fields.Integer('Nro. Tarima')
    cant_bag = fields.Integer('Cantidad de Bultos')
    subtotal_pallet = fields.Integer('Subtotal Tarimas')
    subtotal_bag = fields.Integer('Subtotal Bultos')
    merc_type = fields.Char('Tipo de Mercadería')
    pallet_state = fields.Selection([
        ('a', 'Armado'),
        ('m', 'Mantenimiento'),
        ('t', 'Transitorio')
    ], string='Estado de Tarima')
