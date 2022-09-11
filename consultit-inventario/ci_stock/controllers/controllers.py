# -*- coding: utf-8 -*-
# from odoo import http


# class CiStock(http.Controller):
#     @http.route('/ci_stock/ci_stock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ci_stock/ci_stock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ci_stock.listing', {
#             'root': '/ci_stock/ci_stock',
#             'objects': http.request.env['ci_stock.ci_stock'].search([]),
#         })

#     @http.route('/ci_stock/ci_stock/objects/<model("ci_stock.ci_stock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ci_stock.object', {
#             'object': obj
#         })
