# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class HrAppraisal(models.Model):
    _inherit = 'hr.appraisal'

    period_id = fields.Many2one('hr.appraisal.period', string='Período de Evaluación')
    date_next = fields.Date('Próxima Revisión')
    observations = fields.Text('Observaciones')
    employee_identification_id = fields.Char('Nro. Identificación', related='employee_id.identification_id')
    employee_firstname = fields.Char('Nombres', related='employee_id.firstname')
    employee_lastname = fields.Char('Primer Apellido', related='employee_id.lastname')
    employee_lastname2 = fields.Char('Segundo Apellido', related='employee_id.lastname2')
    competence_ids = fields.One2many('hr.appraisal.competence', 'appraisal_id', string='Competencias')
    goal_ids = fields.One2many('hr.appraisal.goal', 'appraisal_id', string='Metas y Objetivos')
    note_id = fields.Many2one('hr.appraisal.note', string='Tabla de Evaluación')