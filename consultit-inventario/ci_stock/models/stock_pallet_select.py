# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class StockPalletSelect(models.Model):
    _name = 'stock.pallet.select'
    _rec_name = 'name'

    name = fields.Char('name')