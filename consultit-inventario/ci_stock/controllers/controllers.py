# -*- coding: utf-8 -*-
# from odoo import http


# class HaStock(http.Controller):
#     @http.route('/ha_stock/ha_stock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ha_stock/ha_stock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ha_stock.listing', {
#             'root': '/ha_stock/ha_stock',
#             'objects': http.request.env['ha_stock.ha_stock'].search([]),
#         })

#     @http.route('/ha_stock/ha_stock/objects/<model("ha_stock.ha_stock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ha_stock.object', {
#             'object': obj
#         })
