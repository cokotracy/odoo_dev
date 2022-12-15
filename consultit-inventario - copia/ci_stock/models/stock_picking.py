# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    control_id = fields.Many2one('stock.cargo.entry.control', 'Hoja de control de Ingreso')
    pallet_select_ids = fields.Many2many('stock.pallet.select', string='pallet_select')
