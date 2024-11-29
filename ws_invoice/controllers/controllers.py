# -*- coding: utf-8 -*-
# from odoo import http


# class WsInvoice(http.Controller):
#     @http.route('/ws_invoice/ws_invoice', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ws_invoice/ws_invoice/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ws_invoice.listing', {
#             'root': '/ws_invoice/ws_invoice',
#             'objects': http.request.env['ws_invoice.ws_invoice'].search([]),
#         })

#     @http.route('/ws_invoice/ws_invoice/objects/<model("ws_invoice.ws_invoice"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ws_invoice.object', {
#             'object': obj
#         })
