# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models, _


class StockBatch(models.Model):
    _name = 'stock.batch'
    _description = 'Batch'
    # _rec_name = 'nro_doc'

    nro_batch = fields.Char('Nro. Batch')
    cargo_entry_id = fields.Many2one('stock.cargo.entry.control', string='Control de Ingreso de Carga')
    pallet_id = fields.Many2one('stock.pallet', 'Tarima')
    cant_bag = fields.Integer('Cant. Bultos')
    cant_pallet = fields.Integer('Cant. Tarimas')
    subtotal_pallet = fields.Integer('Subtotal Tarimas')
    subtotal_bag = fields.Integer('Subtotal Bultos')
    merc_type = fields.Char('Tipo Mercadería')
    pallet_state = fields.Selection([
        ('a', 'Armado'),
        ('m', 'Mantenimiento'),
        ('t', 'Transitorio')
    ], string='Estado Tarima')
    nro_pedido = fields.Char('Pedido')
    vendor = fields.Char('Vendor')
    lot_id = fields.Many2one('stock.production.lot', 'Lote')
    nro_orden = fields.Char('Orden')
    product_id = fields.Many2one('product.template', 'Producto')
    cant = fields.Integer('Cant. Producto')
    pallet_select_ids = fields.Many2many('stock.pallet.select', string='pallet_select')
    
