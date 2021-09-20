# -*- coding: utf-8 -*-
from odoo import fields, models, api, http
from datetime import datetime, timedelta


class homeConfigure(models.Model):
    _name = "banner.banner"

    sequence = fields.Integer('Sequence')
    active_style_1 = fields.Boolean('Banner Style Active 1')
    banner_style_1_ids = fields.One2many('banner.style1', 'banner_style_1_id', string='Home Banner')
    active_style_2 = fields.Boolean('Banner Style Active 2')
    banner_style_2_ids = fields.One2many('banner.style2', 'banner_style_2_id', string='Home Banner')
    category_style_2_ids = fields.One2many('category.banner.style2', 'category_style_2_id', string='Home Banner Category')
    active_style_3 = fields.Boolean('Banner Style Active 3')
    banner_style_3_ids = fields.One2many('banner.style3', 'banner_style_3_id', string='Home Banner')
    active_style_4 = fields.Boolean('Banner Style Active 4')
    banner_style_4_ids = fields.One2many('banner.style4', 'banner_style_4_id', string='Home Banner')
    active_style_5 = fields.Boolean('Banner Style Active 5')
    banner_style_5_ids = fields.One2many('banner.style5', 'banner_style_5_id', string='Home Banner')
    image1_style_5 = fields.Binary('Banner Image 1')
    image2_style_5 = fields.Binary('Banner Image 2')
    image3_style_5 = fields.Binary('Banner Image 3')
    active_style_6 = fields.Boolean('Banner Style Active 6')
    banner_style_6_ids = fields.One2many('banner.style6', 'banner_style_6_id', string='Home Banner')
    active_style_7 = fields.Boolean('Banner Style Active 7')
    banner_style_7_ids = fields.One2many('banner.style7', 'banner_style_7_id', string='Home Banner')


class homeBanner1Configure(models.Model):
    _name = "banner.style1"

    banner_style_1_id = fields.Many2one('banner.banner', string='Home Banner')
    image = fields.Binary('Image')
    product_title = fields.Char('Title')
    product_name = fields.Char('Name')
    product_description = fields.Char('Description')
    url = fields.Char('Url')


class homeBanner2Configure(models.Model):
    _name = "banner.style2"

    banner_style_2_id = fields.Many2one('banner.banner', string='Home Banner')
    image = fields.Binary('Image')
    product_title = fields.Char('Title')
    product_name = fields.Char('Name')
    product_description = fields.Char('Description')
    url = fields.Char('Url')

class homeCategoryBanner2Configure(models.Model):
    _name = "category.banner.style2"

    category_style_2_id = fields.Many2one('banner.banner', string='Home Banner Category')
    image = fields.Binary('Image')
    name = fields.Char('Name')
    url = fields.Char('Url')


class homeBanner3Configure(models.Model):
    _name = "banner.style3"

    banner_style_3_id = fields.Many2one('banner.banner', string='Home Banner')
    image = fields.Binary('Image')
    product_title = fields.Char('Title')
    product_name = fields.Char('Name')
    product_description = fields.Char('Description')
    url = fields.Char('Url')


class homeBanner4Configure(models.Model):
    _name = "banner.style4"

    banner_style_4_id = fields.Many2one('banner.banner', string='Home Banner')
    image = fields.Binary('Image')
    product_title = fields.Char('Title')
    product_name = fields.Char('Name')
    product_description = fields.Char('Description')
    url = fields.Char('Url')


class homeBanner5Configure(models.Model):
    _name = "banner.style5"

    banner_style_5_id = fields.Many2one('banner.banner', string='Home Banner')
    image = fields.Binary('Image')
    product_title = fields.Char('Title')
    product_name = fields.Char('Name')
    product_description = fields.Char('Description')
    url = fields.Char('Url')


class homeBanner6Configure(models.Model):
    _name = "banner.style6"

    banner_style_6_id = fields.Many2one('banner.banner', string='Home Banner')
    image = fields.Binary('Image')
    product_title = fields.Char('Title')
    product_name = fields.Char('Name')
    product_description = fields.Char('Description')
    url = fields.Char('Url')


class homeBanner7Configure(models.Model):
    _name = "banner.style7"

    banner_style_7_id = fields.Many2one('banner.banner', string='Home Banner')
    image = fields.Binary('Image')
    product_title = fields.Char('Title')
    product_name = fields.Char('Name')
    product_description = fields.Char('Description')
    url = fields.Char('Url')


class homeSummerSale(models.Model):
    _name = "summer.sale"

    sequence = fields.Integer('Sequence')
    summer_sale_style_1_ids = fields.One2many('summer.sale1', 'summer_sale_style_1_id', string='Summer Sale')
    summer_sale_style_2_ids = fields.One2many('summer.sale2', 'summer_sale_style_2_id', string='Summer Sale')
    summer_sale_style_3_ids = fields.One2many('summer.sale3', 'summer_sale_style_3_id', string='Summer Sale')


class homeSummerSale1(models.Model):
    _name = "summer.sale1"

    summer_sale_style_1_id = fields.Many2one('summer.sale', string='Summer Sale Style 1')
    active_style_1 = fields.Boolean('Summer Sale Style Active 1')
    sale_description_style_1 = fields.Html('Summer Sale Description')
    sale_promo_code_style_1 = fields.Html('Summer Sale Promo Code')

class homeSummerSale2(models.Model):
    _name = "summer.sale2"

    summer_sale_style_2_id = fields.Many2one('summer.sale', string='Summer Sale Style 2')
    active_style_2 = fields.Boolean('Summer Sale Style Active 2')
    sale_description_style_2 = fields.Html('Summer Sale Description')
    sale_promo_code_style_2 = fields.Html('Summer Sale Promo Code')

class homeSummerSale3(models.Model):
    _name = "summer.sale3"

    summer_sale_style_3_id = fields.Many2one('summer.sale', string='Summer Sale Style 3')
    active_style_3 = fields.Boolean('Summer Sale Style Active 3')
    sale_description_style_3 = fields.Html('Summer Sale Description')
    sale_promo_code_style_3 = fields.Html('Summer Sale Promo Code')