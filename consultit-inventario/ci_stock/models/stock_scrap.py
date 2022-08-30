# -*- coding: utf-8 -*-

from dataclasses import field
from odoo import api, fields, models, _


class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    picking_id = fields.Many2one('stock.picking', 'Transferencia')
    partner_id = fields.Many2one('res.partner', 'Proveedor')
    date = fields.Date('Fecha')
    po_line = fields.Char('Nro. PO y Línea')
    nro_invoice = fields.Char('Nro. Factura')
    nro_material = fields.Char('Nro. Material')
    cant_received = fields.Integer('Cantidad Recibida')
    cant_rejected = fields.Integer('Cantidad Rechazada')
    nro_container = fields.Char('Nro. Contenedor')
    description = fields.Text('Decripción')
    recibo = fields.Char('Recibido por')
    revisado = fields.Char('Revisado por')
    desc_damage = fields.Selection([
        ('d', 'Derrame'),
        ('g', 'Golpe y Fuga'),
        ('c', 'Contaminado'),
        ('s', 'Sellos'),
        ('o', 'Otro'),
    ], string='Decripción de daños')
    other_description = fields.Char('Otra descripción')
    batch_id = fields.Many2one('stock.picking.batch', 'Vendor batch de material')
    images_ids = fields.One2many('stock.scrap.image', 'scrap_id', string='Imágenes')
    vendor_batch_material = fields.Char('Vendor batch de material')


class StockScrapImage(models.Model):
    _name = 'stock.scrap.image'
    
    image = fields.Binary('Imagen')
    scrap_id = fields.Many2one('stock.scrap', 'Imagen')