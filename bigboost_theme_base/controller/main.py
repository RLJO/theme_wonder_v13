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
        return request.render('bigboost_theme_base.homepage_template', {})


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
            print("======ppg_shop=====",int(post.get('ppg_shop')))
            request.env['website'].get_current_website().write({
                'shop_ppg':int(post.get('ppg_shop'))
            })
        return True