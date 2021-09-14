from odoo import fields, models, http


class PublicCategory(models.Model):
    _inherit = "product.public.category"

    description = fields.Text('Description')
