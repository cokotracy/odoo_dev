# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    control_id = fields.Many2one('stock.cargo.entry.control', 'Hoja de control de Ingreso')
    level = fields.Char('Nivel Ubicado')
    pallet_select_ids = fields.Many2many('stock.pallet.select', string='pallet_select')
    # Importados de otro módulo
    dua = fields.Many2one('stock.dua', 'Nro. de DUA de ingreso', related="control_id.dua")
    nro_bl = fields.Char('Nro. BL')
    nro_viaje = fields.Char('Nro. Viaje')
    nro_ut = fields.Char('Nro. UT')
    fecha_ingreso = fields.Date('Fecha Ingreso', related="control_id.date")
    mercaderia = fields.Text('Mercadería')
    bag = fields.Integer('Bultos', related='control_id.total_bulto')
    pallet = fields.Integer('Tarimas', related='control_id.total_tarima')
    peso = fields.Float('Peso')
    manifiesto = fields.Char('Manifiesto')
    consignatario = fields.Char('Consignatario')
    name_edit = fields.Char('Mov. Inv.')


class StockPalletSelect(models.Model):
    _name = 'stock.pallet.select'
    _rec_name = 'name'

    name = fields.Char('name')