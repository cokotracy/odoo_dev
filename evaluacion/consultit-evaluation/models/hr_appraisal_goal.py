# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date


class HrAppraisalGoal(models.Model):
    _inherit = 'hr.appraisal.goal'

    appraisal_id = fields.Many2one('hr.appraisal', 'Evaluación')
    activity_id = fields.Many2one('hr.appraisal.remedial.activity', 'Actividad Remedial')
    type = fields.Selection([('objetivo', 'Objetivo'),
                             ('meta', 'Meta')], string='Tipo')
    year = fields.Integer('Año', default=date.today().year)
    date_start = fields.Date('Fecha asignación', default=fields.Date.today())
    date_end = fields.Date('Fecha Cuminación')
    percentage_complete = fields.Float('Porcentaje cumplido')