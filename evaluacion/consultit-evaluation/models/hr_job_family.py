# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HrJobFamily(models.Model):
    _name = 'hr.job.family'
    _description = 'Familia de cargos'
    _rec_name = 'description'

    description = fields.Char(u'Descripción')
    level1 = fields.Float(u'Nivel 1: PEN, PNDIP, PS')
    level2 = fields.Float(u'Nivel 2: PEI, POI')
    level3 = fields.Float(u'Nivel 3: Usuarios / Contraloría')
    level4 = fields.Float(u'Nivel 4: PEI, POI')
    level5 = fields.Float(u'Nivel 5: PEI, POI')
    level6 = fields.Float(u'Competencias Individuales')
    level7 = fields.Float(u'Autoevaluación')
    level8 = fields.Float(u'Colaboradores')
    total = fields.Float('Total', compute='_compute_total')

    @api.depends('level1', 'level2', 'level3', 'level4', 'level5', 'level6', 'level7', 'level8')
    def _compute_total(self):
        self.total = (self.level1 + self.level2 + self.level3 + self.level4 + 
                      self.level5 + self.level6 + self.level7 + self.level8)
