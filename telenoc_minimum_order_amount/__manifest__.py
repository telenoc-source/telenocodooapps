# -*- coding: utf-8 -*-

{
    'name': 'Tele Minimum Order Amount Restriction',
    'version': '17.0.1.0.0',
    'summary': """The Minimum Order Amount App for odoo empowers your e-commerce business with the ability
    to set minimum order requirement to complete a purchase.""",
    'category': 'eCommerce',
    'author': 'TeleNoc',
    'company': 'TeleNoc',
    'website': "https://telenoc.org",
    'depends': ['base', 'website', 'website_sale', 'mail', 'account'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/templates.xml',
    ],
    'images': ['static/description/banner.jpeg'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
