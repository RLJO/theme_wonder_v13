# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_new_product = fields.Boolean(string='New Product')
    website_details = fields.Html(string='Website Details')
    product_video_url = fields.Char(string='Product Video URL')
    timer = fields.Date(string="Offer Date")

class ProductPublicCategory(models.Model):
    _inherit = 'product.public.category'

    is_display_product = fields.Boolean(string='Is Display Product Page')
