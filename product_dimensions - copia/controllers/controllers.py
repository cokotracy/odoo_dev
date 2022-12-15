# -*- coding: utf-8 -*-
# from odoo import http


# class ProductDimensions(http.Controller):
#     @http.route('/product_dimensions/product_dimensions', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_dimensions/product_dimensions/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_dimensions.listing', {
#             'root': '/product_dimensions/product_dimensions',
#             'objects': http.request.env['product_dimensions.product_dimensions'].search([]),
#         })

#     @http.route('/product_dimensions/product_dimensions/objects/<model("product_dimensions.product_dimensions"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_dimensions.object', {
#             'object': obj
#         })
