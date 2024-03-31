# -*- coding: utf-8 -*-
{
    'name': 'Tele Point of Sale Logo',
    'version': '17.0.1.0.0',
    'category': 'Point of Sale',
    'summary': "Logo For Every Point of Sale (Screen & Receipt)",
    'description': "This module helps you to set a logo for every POS"
                   "This will help you to identify the point of sale easily."
                   "You can also see this logo in pos screen and pos receipt.",
    'author': 'TeleNoc',
    'company': 'TeleNoc',
    'maintainer': "TeleNoc",
    'website': "http://www.telenoc.org",
    'depends': ['point_of_sale'],
    'data': ['views/pos_config_views.xml'],
    'assets': {
        'point_of_sale._assets_pos': [
            'point_of_sale_logo/static/src/xml/navbar_logo.xml',
            'point_of_sale_logo/static/src/xml/receipt_logo.xml'
        ],
    },
    'images': ['static/description/banner.jpeg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
