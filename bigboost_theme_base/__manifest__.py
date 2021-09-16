# -*- coding: utf-8 -*-


{
    # Theme information
    'name': 'Bigboost Theme Base',
    'category': 'Base',
    'summary': 'Base module containing common libraries for all Emipro eCommerce themes.',
    'version': '2.2.1',
    'depends': [
        'website_theme_install',
        'website_sale_wishlist',
	    'website_sale_comparison',
        'website_blog',
        'portal',
    ],

    'data': [
	    'security/ir.model.access.csv',

        'views/res_config_settings.xml',
        'views/blog_view.xml',
        'views/shop.xml',
        'views/public_category_view.xml',
        'views/portal.xml',
        'views/product_template_view.xml',
        'views/home.xml',

    ],
    # Author
    'author': 'Bansi',
    # Technical
    'installable': True,
    'auto_install': False,

}
