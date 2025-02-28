# -*- coding: utf-8 -*-
# from odoo import http


# class Cms(http.Controller):
#     @http.route('/cms/cms', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cms/cms/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cms.listing', {
#             'root': '/cms/cms',
#             'objects': http.request.env['cms.cms'].search([]),
#         })

#     @http.route('/cms/cms/objects/<model("cms.cms"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cms.object', {
#             'object': obj
#         })

