# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models, _


class StockChecklist(models.Model):
    _name = 'stock.cargo.entry.control'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hoja de Control de Ingreso de Carga'
    _rec_name = 'sheet_number'

    sheet_number = fields.Char('Nro. Hoja Control')
    customer_id = fields.Many2one('res.partner', 'Cliente')
    nro_container = fields.Many2one('stock.container', 'Contenedor')
    dua = fields.Many2one('stock.dua', 'DUA')
    mov_tica = fields.Char('Movimiento TICA')
    chamberos = fields.Boolean('Requiere Chamberos')
    date = fields.Date('Fecha')
    hora_ingreso = fields.Float('Hora ingreso Transporte a andén')
    hora_inicio = fields.Float('Hora inicio descarga')
    hora_fin = fields.Float('Hora fin descarga')
    cant_personas = fields.Integer('Cantidad personas descargando')
    po = fields.Char('PO')
    nota_embarque = fields.Text('Nota embarque')
    despal_fracc = fields.Integer('Despaletizado o fraccionamiento')
    faltante = fields.Integer('Faltante')
    total_tarima = fields.Integer('Gran Total Tarimas')
    total_bulto = fields.Integer('Gran Total Bultos')
    observation = fields.Text('Obervaciones')
    responsible = fields.Char('Chequeador HA responsable')
    batch_ids = fields.One2many('stock.batch', 'cargo_entry_id', string='Batch')
    picking_id = fields.Many2one('stock.picking', string='Transferencia')
    embalaje_ids = fields.Many2many('stock.embalaje', string='Embalaje')
    user_id = fields.Many2one('res.users', 'Usuario Asignado a Atender esta carga')
    

    def action_create_stock_move(self):
        return {
            'res_model': 'stock.picking',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref('stock.view_picking_form').id,
            'target': self
        }

    def action_user_notification(self):
        for rec in self:
            message = 'Nueva entrada asignada para ' + str(rec.user_id.name) 
            notification = rec.user_id.notify_info(message)
            msg = rec.message_post(body=message, subject="Entrada creada")
        return notification, msg
"""
    def action_user_message(self):
        for rec in self:
            message = 'Nueva entrada asignada para ' + str(rec.user_id.name)
            msg = rec.user_id.message_post(message)
            notfi = rec.user_id.notify_info(message)
        return msg, notfi
"""
            

class StockEmbalaje(models.Model):
    _name = 'stock.embalaje'

    name = fields.Char('name')


