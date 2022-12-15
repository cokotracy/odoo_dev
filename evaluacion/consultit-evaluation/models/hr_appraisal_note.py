# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class HrAppraisal(models.Model):
    _inherit = 'hr.appraisal.note'

    value = fields.Float('Valor')
    description = fields.Text('Descripción')
