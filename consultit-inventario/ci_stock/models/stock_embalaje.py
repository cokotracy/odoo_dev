# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, _


class StockEmbalaje(models.Model):
    _name = 'stock.embalaje'

    name = fields.Char('name')