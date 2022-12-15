# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HrAppraisalRemedialActivity(models.Model):
    _name = 'hr.appraisal.remedial.activity'
    _description = 'Actividad Remedial'
    _rec_name = 'description'

    description = fields.Char('Descripción')
    time_req = fields.Integer('Tiempo Requerido (Días)')
    time_start = fields.Integer('Iniciar en (Días)')
    observations = fields.Char('Observaciones')
    job_id = fields.Many2one('hr.job', string='Cargo')
    appraisal_id = fields.Many2one('hr.appraisal', 'Evaluación')
    area_id = fields.Many2one('hr.form.area', string='Área de Formación')