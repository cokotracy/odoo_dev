# -*- coding: utf-8 -*-
# Powered by Cereza Technology.
# © 2022 Cereza Technology. (<https://cerezatechnology.com/>)

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    pet_ids = fields.One2many('res.partner.pet', 'partner_id', string='Pets')

    