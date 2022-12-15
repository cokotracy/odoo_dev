# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class DepartmentTime(models.Model):
    _name = 'hr.department.time'
    _description = 'Horario de Departamento'
    _rec_name = 'description'

    department_id = fields.Many2one('hr.department', 'Departamento')
    days_off = fields.Integer(u'Días Libres')
    time_start = fields.Float('Hora Inicio')
    time_end = fields.Float('Hora Fin')
    time_off_start = fields.Float('Inicio Descanso')
    time_off_end = fields.Float('Fin Descanso')
    description = fields.Char(u'Descripción Horario')