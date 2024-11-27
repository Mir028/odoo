# -*- coding: utf-8 -*-
# from odoo import http


# class WsOrder(http.Controller):
#     @http.route('/ws_order/ws_order', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ws_order/ws_order/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ws_order.listing', {
#             'root': '/ws_order/ws_order',
#             'objects': http.request.env['ws_order.ws_order'].search([]),
#         })

#     @http.route('/ws_order/ws_order/objects/<model("ws_order.ws_order"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ws_order.object', {
#             'object': obj
#         })
