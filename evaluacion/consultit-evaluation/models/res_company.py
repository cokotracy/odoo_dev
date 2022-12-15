# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = "res.company"

    date_registry = fields.Date('Fecha Registro')