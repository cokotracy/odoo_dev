# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class StockCargoEntryControl(models.Model):
    _name = 'stock.cargo.entry.control'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hoja de Control de Ingreso de Carga'
    _rec_name = 'sheet_number'

    sheet_number = fields.Char('Nro. Hoja Control')
    user_id = fields.Many2one('res.users', 'Usuario Asignado a Atender esta carga')
    picking_id = fields.Many2one('stock.picking', string='Transferencia')
    container_id = fields.Many2one('stock.fleet.container', 'Nro. Contenedor')
    customer_id = fields.Many2one('res.partner', 'Cliente')
    dua_id = fields.Many2one('stock.dua', 'Nro. DUA')
    #Pendiente embalaje_ids batch_ids
    mov_tica = fields.Char('Movimiento TICA', related='dua_id.mov_tica')
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

    def action_user_notification(self):
        for rec in self:
            message = 'Nueva entrada asignada para ' + str(rec.user_id.name) 
            notification = rec.user_id.notify_info(message)
            msg = rec.message_post(body=message, subject="Entrada creada")
        return notification, msg

    def action_create_stock_move(self):
        """Button to generate stock picking move"""
        print('Stock Move')
        pass