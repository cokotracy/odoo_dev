# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models, _


class StockChecklist(models.Model):
    _name = 'stock.cargo.entry.control'
    _description = 'Hoja de Control de Ingreso de Carga'
    _rec_name = 'customer_id'

    customer_id = fields.Many2one('res.partner', 'Cliente')
    nro_container = fields.Char('Nro. de Contenedor')
    dua = fields.Char('Nro. de DUA de ingreso')
    chamberos = fields.Boolean('Requiere Chamberos')
    date = fields.Date('Fecha')
    hora_ingreso = fields.Float('Hora ingreso de Transporte a andén')
    hora_inicio = fields.Float('Hora inicio de descarga')
    hora_fin = fields.Float('Hora fin de descarga')
    cant_personas = fields.Integer('Cantidad personas descargando')
    po = fields.Char('PO')
    nota_embarque = fields.Text('Nota de embarque')
    despal_fracc = fields.Integer('Despaletizado o fraccionamiento')
    faltante = fields.Integer('Faltante')
    embalaje = fields.Selection([
        ('b', 'Bien'),
        ('a', 'Abierto'),
        ('h', 'Húmedo'),
        ('v', 'Vacío'),
        ('g', 'Golpeado'),
        ('r', 'Roto'),
        ('q', 'Quebrado')
    ], string='Seleccione embalaje de acuerdo al ingreso')
    total_tarima = fields.Integer('Gran Total Tarimas')
    total_bulto = fields.Integer('Gran Total Bultos')
    observation = fields.Text('Obervaciones')
    responsible = fields.Char('Chequeador HA responsable')
    batch_ids = fields.One2many('stock.batch', 'cargo_entry_id', string='Batch')
    picking_id = fields.Many2one('stock.picking', string='Transferencia')
    

    def action_create_stock_move(self):
        return {
            'res_model': 'stock.picking',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref('stock.view_picking_form').id,
            'target': self,
        }