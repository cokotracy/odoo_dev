# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HrAppraisalPeriod(models.Model):
    _name = 'hr.appraisal.period'
    _description = 'Período de Evaluación'
    _rec_name = 'year'

    date_start = fields.Date('Fecha Inicio')
    date_end = fields.Date('Fecha Finalización')
    year = fields.Integer(u'Año')
    appraisal_ids = fields.One2many('hr.appraisal', 'period_id', string='Evaluaciones')