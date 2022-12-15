# -*- coding: utf-8 -*-
# Powered by Cereza Technology.
# © 2022 Cereza Technology. (<https://cerezatechnology.com/>)

from odoo import api, fields, models


class ResPartnerPet(models.Model):
    _name = "res.partner.pet"

    name = fields.Char(string='Pet Name', required=True)
    specie = fields.Selection([
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('rodent', 'Rodent'),
        ('bird', 'Bird'),
        ('fish', 'Fish'),
        ('reptile', 'Reptile'),
        ('horse', 'Horse')], string='Specie')
    pet_birthday = fields.Date(string='Pet Birthday')
    partner_id = fields.Many2one('res.partner', string='Owner')
    company_id = fields.Many2one('res.company', 'Company', index=True)
    sex = fields.Selection([('female', 'Female'), ('male', 'Male')], string='Sex')
    race = fields.Char(string='Race')
    color = fields.Char(string='Color')
    holding_reason = fields.Selection([
        ('company', 'Company'),
        ('attendance', 'Attendance'),
        ('therapy', 'Therapy'),
        ('work', 'Work'),
        ('security', 'Security'),
        ('sports', 'Sports'),
        ('exhibition', 'Exhibition'),
        ('reproduction', 'Reproduction'),
        ('hunting', 'Hunting')], string='Holding Reason')
    send_birthday_email = fields.Boolean(string="Send Brithday Email")
    image = fields.Binary(string="Pet Image")
    sterilized_castrated = fields.Boolean(string="Sterilized/Castrated")
    weight = fields.Integer(string="Weight")
    pleasures = fields.Text(string="Pleasures")
    nutritional_conditions = fields.Text(string="Nutritional Conditions")
    activity = fields.Char(string="Activity")
    special_cares = fields.Text(string="Special Cares")
    toys = fields.Text(string="Toys")

    @api.model
    def _send_birthday_email(self):
        birthday = self.pet_birthday
        today = fields.Date.context_today(self)
        for pet in self.env['res.partner.pet'].search([('pet_birthday', '!=', False), ('partner_id.email', '!=', False)]):
            if pet.send_birthday_email and today == pet.pet_birthday:
                pass

