# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, _


class StockCargoOutputControl(models.Model):
    _name = 'stock.cargo.output.control'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hoja de Control de Salida de Carga'
    _rec_name = 'sheet_number'

    sheet_number = fields.Char('Nro. Hoja Control')
    customer_id = fields.Many2one('res.partner', 'Cliente')
    user_id = fields.Many2one('res.users', 'Usuario Asignado a Atender esta carga')
    container_id = fields.Many2one('stock.fleet.container', 'Nro. Contenedor')
    picking_ids = fields.One2many('stock.picking', 'control_id', string='Transferencias')
    picking_count = fields.Integer(string='Pickings', compute='_compute_picking_count')
    picking_type_id = fields.Many2one('stock.picking.type', 'Operation Type')
    location_id = fields.Many2one('stock.location', "Source Location")
    location_dest_id = fields.Many2one('stock.location', "Destination Location")
    date = fields.Date('Fecha')
    responsible = fields.Char('Chequeador HA responsable')
    observation = fields.Text('Obervaciones')
    batch_ids = fields.One2many('stock.batch', 'cargo_entry_id', string='batch')

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