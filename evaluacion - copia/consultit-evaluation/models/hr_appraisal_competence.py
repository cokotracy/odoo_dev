# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HrAppraisalCompetence(models.Model):
    _name = 'hr.appraisal.competence'
    _description = 'Competencias'
    _rec_name = 'description'

    appraisal_id = fields.Many2one('hr.appraisal', 'Evaluación')
    activity_id = fields.Many2one('hr.appraisal.remedial.activity', 'Actividad Remedial')
    description = fields.Char('Descripción')
    percentage_dominance = fields.Selection(selection=[
        ('0', '0 %'),
        ('25', '25 %'),
        ('50', '50 %'),
        ('75', '75 %'),
        ('100', '100 %')
    ], string="Dominance", default="0", required=False)
    observations = fields.Text('Observaciones')
    employee_id = fields.Many2one('hr.employee', string='Empleado', related="appraisal_id.employee_id")
    job_id = fields.Many2one('hr.job', string='Cargo', related="appraisal_id.job_id")
    date_act = fields.Date('Fecha Actualización')
    