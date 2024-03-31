# -*- coding: utf-8 -*-


{
    'name': 'Tele POS Custom Receipt',
    'version': '1.0',
    "license": "OPL-1",
    'depends': ['base', 'point_of_sale'],
    'category': 'Sales/Point of Sale',
    'author': 'TeleNoc',
    'summary': 'This module is used to customized receipt of point of sale when a user adds a product in the cart and validates payment and print receipt, then the user can see the client name on POS Receipt. | Custom Receipt | POS Reciept | Payment | POS Custom Receipt',
    'description': "Customized our point of sale receipt.",
    'assets': {
        'point_of_sale._assets_pos': [
            'tele_custom_pos_receipt/static/src/**/*',
        ],
    },
    'images': ['static/description/banner.jpeg'],
    'installable': True,
}
