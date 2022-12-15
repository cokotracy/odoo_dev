# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HrAppraisalPlan(models.Model):
    _inherit = 'hr.appraisal.plan'

    name = fields.Char('Plan')
    code = fields.Char('Código')
    observations = fields.Char('Iniciar en (Días):')
    family_id = fields.Many2one('hr.job.family', string='Familia de Cargos')