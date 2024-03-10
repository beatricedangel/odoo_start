# -*- coding: utf-8 -*-
# from odoo import http


# class Prenotazioni(http.Controller):
#     @http.route('/prenotazioni/prenotazioni/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prenotazioni/prenotazioni/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prenotazioni.listing', {
#             'root': '/prenotazioni/prenotazioni',
#             'objects': http.request.env['prenotazioni.prenotazioni'].search([]),
#         })

#     @http.route('/prenotazioni/prenotazioni/objects/<model("prenotazioni.prenotazioni"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prenotazioni.object', {
#             'object': obj
#         })
