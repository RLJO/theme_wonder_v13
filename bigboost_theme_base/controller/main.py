# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by 73lines
# See LICENSE file for full copyright and licensing details.


from datetime import datetime
from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website
from odoo.addons.website_sale.controllers.main import WebsiteSale


class Website(Website):

    @http.route('/', type='http', auth="public", website=True)
    def index(self, **kw):
        banners = request.env['banner.banner'].sudo().search([])
        sales = request.env['summer.sale'].sudo().search([])
        return request.render('bigboost_theme_base.homepage_template', {
            'banners': banners,
            'sales': sales,
        })


class WebsiteSaleInherit(WebsiteSale):

    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        res = super(WebsiteSaleInherit, self).shop(page=page,
                                                    category=category,
                                                    search=search, ppg=ppg,
                                                    **post)
        print("\n\n\n=========UPDATED========CONTENT==========",res)
        # res.qcontext.update({
        #     'get_attribute_value_ids': self.get_attribute_value_ids,
        # })
        return res


class WebsiteController(http.Controller):

    # Shop Page PPG Change Json Route
    @http.route(['/ppg_shop/update'], type='json', auth="public", method='post', website=True)
    def ppg_shop_update(self, **post):
        if post.get('ppg_shop'):
            request.env['website'].get_current_website().sudo().write({
                'shop_ppg':int(post.get('ppg_shop'))
            })
        return True

    # CREATE PRODUCT REVIEW FORM SAVE DATA
    @http.route(['/review-created'], type='http', auth="public", methods=['POST'], website=True)
    def product_review_created(self, **post):
        if post.get("name") and post.get("product_id"):
            product = request.env['product.template'].sudo().browse([int(post.get("product_id"))])
            product_review = request.env['product.review'].sudo().create({
                'product_id':product.id,
                'name':post.get("name"),
                'email':post.get("email"),
                'title':post.get("title"),
                'description':post.get("description"),
                'state':post.get("stars"),
            })
        return request.render('bigboost_theme_base.thank_you_review_template', {'product':product})

    # Product add to Cart by Popup
    @http.route(['/custom_cart'], type='json', auth="public", method='post', website=True)
    def custom_cart(self, **post):
        if post.get('product_template_id') and post.get('add_qty'):
            order = request.website.sale_get_order(force_create=True)
            order._cart_update(
                product_id=int(post.get('product_template_id')),
                add_qty=int(post.get('add_qty')),
            )
        return True