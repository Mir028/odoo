# -*- coding: utf-8 -*-
# from odoo import http


# class WsPurchase(http.Controller):
#     @http.route('/ws_purchase/ws_purchase', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ws_purchase/ws_purchase/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ws_purchase.listing', {
#             'root': '/ws_purchase/ws_purchase',
#             'objects': http.request.env['ws_purchase.ws_purchase'].search([]),
#         })

#     @http.route('/ws_purchase/ws_purchase/objects/<model("ws_purchase.ws_purchase"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ws_purchase.object', {
#             'object': obj
#         })
