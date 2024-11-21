# -*- coding: utf-8 -*-
# from odoo import http


#class Joby(http.Controller):

#     @http.route('/joby/joby', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/joby/joby/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('joby.listing', {
#             'root': '/joby/joby',
#             'objects': http.request.env['joby.joby'].search([]),
#         })

#     @http.route('/joby/joby/objects/<model("joby.joby"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('joby.object', {
#             'object': obj
#         })

