# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, _


class StockCargoEntryControl(models.Model):
    _name = 'stock.cargo.entry.control'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hoja de Control de Ingreso de Carga'
    _rec_name = 'sheet_number'

    sheet_number = fields.Char('Nro. Hoja Control')
    user_id = fields.Many2one('res.users', 'Usuario Asignado a Atender esta carga')
    picking_ids = fields.One2many('stock.picking', 'control_id', string='Transferencias')
    picking_type_id = fields.Many2one('stock.picking.type', 'Operation Type')
    location_id = fields.Many2one('stock.location', "Source Location")
    location_dest_id = fields.Many2one('stock.location', "Destination Location")
    container_id = fields.Many2one('stock.fleet.container', 'Nro. Contenedor')
    customer_id = fields.Many2one('res.partner', 'Cliente')
    dua_id = fields.Many2one('stock.dua', 'Nro. DUA')
    mov_tica = fields.Char('Movimiento TICA')
    chamberos = fields.Boolean('Requiere Chamberos')
    date = fields.Date('Fecha')
    hora_ingreso = fields.Float('Hora ingreso Transporte a andén')
    hora_inicio = fields.Float('Hora inicio descarga')
    hora_fin = fields.Float('Hora fin descarga')
    cant_personas = fields.Integer('Cantidad personas descargando')
    po = fields.Char('PO')
    nota_embarque = fields.Text('Nota embarque')
    observation = fields.Text('Obervaciones')
    responsible = fields.Char('Chequeador HA responsable')
    batch_ids = fields.One2many('stock.batch', 'cargo_entry_id', string='batch')
    picking_count = fields.Integer(string='Pickings', compute='_compute_picking_count')
    despal_fracc = fields.Integer('Despaletizado o fraccionamiento')
    faltante = fields.Integer('Faltante')
    total_tarima = fields.Integer('Gran Total Tarimas')
    total_bulto = fields.Integer('Gran Total Bultos')
    embalaje_ids = fields.Many2many('stock.embalaje', string='Embalaje')

    def _compute_picking_count(self):
        for record in self:
            picking_count = self.env['stock.picking'].search_count([('control_id', '=', record.id)])
            record.picking_count = picking_count

    def action_user_notification(self):
        for rec in self:
            message = 'Nueva entrada asignada para ' + str(rec.user_id.name) 
            notification = rec.user_id.notify_info(message)
            msg = rec.message_post(body=message, subject="Entrada creada")
        return notification, msg

    def action_create_picking(self):
        self.ensure_one()
        batch_list = []
        for line in self.batch_ids:
            values = (0, 0, {
                'name': line.description,
                'description_picking': line.description,
                'barcode': line.product_id.barcode,
                'product_id': line.product_id.id,
                'product_uom_qty': line.product_qty,
                'product_uom': line.product_uom,
            })
            batch_list.append(values)
        vals = {
            'control_id': self.id,
            'partner_id': self.customer_id.id,
            'picking_type_id': self.picking_type_id.id,
            'location_id': self.location_id.id,
            'location_dest_id': self.location_dest_id.id,
            'date': datetime.now(),
            'move_ids_without_package': batch_list,
        }
        picking = self.env['stock.picking'].create(vals)
        return picking

    @api.onchange('dua_id')
    def _onchange_dua(self):
        for record in self:
            if record.dua_id:
                record.container_id = record.dua_id.container_id
                record.mov_tica = record.dua_id.mov_tica