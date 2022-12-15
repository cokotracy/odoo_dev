# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Department(models.Model):
    _inherit = 'hr.department'

    code = fields.Char(u'Código Departamento')
    time_ids = fields.One2many('hr.department.time', 'department_id', string='Horario Departamento')