from odoo import models, fields, api, _

class resConfig(models.TransientModel):
    _inherit = 'res.config.settings'


    blog_style = fields.Selection([
        ("style_1", "Style 1 (Left Sidebar)"),
        ("style_2", "Style 2 (Right Sidebar)"),
        ("style_3", "Style 3 (No Sidebar)")], "Select Blog Style", default='style_1')

    shop_style = fields.Selection([
        ("style_1", "Style 1 (Left Sidebar)"),
        ("style_2", "Style 2 (Right Sidebar)"),
        ("style_3", "Style 3 (No Sidebar)"),
        ("style_4", "Style 4 (Sidebar Popup)"),
        ("style_5", "Style 5 (Infinite Scroll)"),
        ("style_6", "Style 6 (Metro)"),
        ("style_7", "Style 7 (Full Width)"),
        ("style_8", "Style 8 (3 Gris)"),
        ("style_9", "Style 9 (6 Grid)")], "Select Shop Style", default='style_1')


    @api.model
    def get_values(self):
        res = super(resConfig, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        blog_style = params.get_param('blog_style')
        shop_style = params.get_param('shop_style')

        res.update(
            blog_style = blog_style or '',
            shop_style = shop_style or '',
        )
        return res

    def set_values(self):
        super(resConfig, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('blog_style', self.blog_style and self.blog_style or '')
        self.env['ir.config_parameter'].sudo().set_param('shop_style', self.shop_style and self.shop_style or '')

