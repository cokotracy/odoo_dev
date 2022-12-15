# -*- coding: utf-8 -*-
# from odoo import http


# class Consultit-evaluation(http.Controller):
#     @http.route('/consultit-evaluation/consultit-evaluation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/consultit-evaluation/consultit-evaluation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('consultit-evaluation.listing', {
#             'root': '/consultit-evaluation/consultit-evaluation',
#             'objects': http.request.env['consultit-evaluation.consultit-evaluation'].search([]),
#         })

#     @http.route('/consultit-evaluation/consultit-evaluation/objects/<model("consultit-evaluation.consultit-evaluation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('consultit-evaluation.object', {
#             'object': obj
#         })
