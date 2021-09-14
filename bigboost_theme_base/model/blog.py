# -*- coding: utf-8 -*-
from odoo import fields, models, api, http
from datetime import datetime, timedelta


class BlogPost(models.Model):
    _inherit = "blog.post"

    image = fields.Binary('Image')
    is_popular_blog = fields.Boolean('Popular Blog')
    blog_comment_ids = fields.One2many('blog.comment', 'comment_id', string='Blog Comments')


class ProductProduct(models.Model):
    _name = 'blog.comment'

    comment_id = fields.Many2one('blog.post', string='Comments')
    name = fields.Char('Name')
    email = fields.Char('Email')
    comment = fields.Char('Comment')
    date = fields.Char('Date', compute='_compute_date', store=True)

    @api.depends('create_date')
    def _compute_date(self):
        for rec in self:
            temp_date = rec.create_date + timedelta(hours=-6, minutes=-30)
            rec.date = temp_date.strftime('%I:%M %p')

