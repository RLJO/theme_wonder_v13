{
    'name': 'Theme Bigboost',
    'category': 'Theme/eCommerce',
    'summary': 'Fully Responsive Odoo Theme suitable for eCommerce Businesses',
    'author': 'Bansi Patel',

    'depends': [
        'website_theme_install',
        'website_sale_wishlist',
        'website_sale_comparison',
        'website_sale',
        'website_sale_stock',
        'bigboost_theme_base',
        'website_crm',
        'auth_oauth',
    ],
    'data': [
        'templates/assets.xml',
        'templates/theme_customise_option.xml',
        'templates/customize.xml',
        'templates/header.xml',
        'templates/footer.xml',
    ],

    'installable': True,
    'auto_install': False,
}
