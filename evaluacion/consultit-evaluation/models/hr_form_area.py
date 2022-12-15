# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HrFormArea(models.Model):
    _name = 'hr.form.area'
    _description = 'Áreas de Formación'
    _rec_name = 'description'

    description = fields.Char('Descripción')
    observations = fields.Text('Observaciones')
    time_req = fields.Integer('Tiempo Requerido (Días)')
    time_start = fields.Integer('Iniciar en (Días)')