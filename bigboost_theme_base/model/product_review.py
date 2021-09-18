from odoo import fields, models, api


class ProductReview(models.Model):
    _name = 'product.review'
    _description = 'Product Review'
    _rec_name = 'product_id'

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    title = fields.Char(string="Review Title")
    description = fields.Text(string="Review Description")
    state = fields.Selection([('poor','Poor'),('fair','Fair'),('good','Good'),('vgood','Very Good'),('excellent','Excellent'),],string="Rating")
    product_id = fields.Many2one("product.template",string="Product")


