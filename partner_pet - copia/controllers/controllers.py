# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerPet(http.Controller):
#     @http.route('/partner_pet/partner_pet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_pet/partner_pet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_pet.listing', {
#             'root': '/partner_pet/partner_pet',
#             'objects': http.request.env['partner_pet.partner_pet'].search([]),
#         })

#     @http.route('/partner_pet/partner_pet/objects/<model("partner_pet.partner_pet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_pet.object', {
#             'object': obj
#         })
