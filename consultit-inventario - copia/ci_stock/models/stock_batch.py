# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models, _


class StockBatch(models.Model):
    _name = 'stock.batch'
    _description = 'Batch'
    _rec_name = 'nro_batch'

    nro_batch = fields.Char('Nro. Batch')
    description = fields.Text('Descripción', required="True")
    nro_pedido = fields.Char('Pedido')
    nro_orden = fields.Char('Orden')
    vendor = fields.Char('Vendor')
    cargo_entry_id = fields.Many2one('stock.cargo.entry.control', string='Control de Ingreso de Carga')
    merc_type = fields.Char('Tipo Mercadería')
    vendor = fields.Char('Vendor')
    product_id = fields.Many2one('product.product', 'Product', ondelete="cascade")
    lot_id = fields.Many2one('stock.production.lot', 'Lot/Serial Number', domain="[('product_id', '=', product_id)]")
    product_uom = fields.Many2one('uom.uom', string='Unit of Measure', domain="[('category_id', '=', product_uom_category_id)]")
    product_uom_category_id = fields.Many2one(related='product_id.uom_id.category_id')
    product_type = fields.Selection(related='product_id.type', readonly=True)
    product_qty = fields.Float(string='Quantity', digits='Product Unit of Measure')
    barcode = fields.Char('Código de Barras')
    cant_bag = fields.Integer('Cant. Bultos')
    cant_pallet = fields.Integer('Cant. Tarimas')
    subtotal_pallet = fields.Integer('Subtotal Tarimas')
    subtotal_bag = fields.Integer('Subtotal Bultos')
            
    @api.onchange('barcode')
    def _onchange_barcode_scan(self):
        product_rec = self.env['product.product']
        if self.barcode:
            product = product_rec.search([('barcode', '=', self.barcode)])
            self.product_id = product.id
            self.product_uom = product.uom_id.id
