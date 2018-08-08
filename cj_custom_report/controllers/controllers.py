# -*- coding: utf-8 -*-
from odoo import http

# class CjHrAttendance(http.Controller):
#     @http.route('/cj_custom_report/cj_custom_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cj_custom_report/cj_custom_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cj_custom_report.listing', {
#             'root': '/cj_custom_report/cj_custom_report',
#             'objects': http.request.env['cj_custom_report.cj_custom_report'].search([]),
#         })

#     @http.route('/cj_custom_report/cj_custom_report/objects/<model("cj_custom_report.cj_custom_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cj_custom_report.object', {
#             'object': obj
#         })