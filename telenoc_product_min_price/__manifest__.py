# -*- coding: utf-8 -*-
{
    'name': "Tele Product Purchase Min Price",

    'summary': """
        Display min purchase price in product form""",

    'description': """
    """,

    'author': "TeleNoc",
    'website': "https://telenoc.org",
    'category': 'Purchase',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],
    'images': ['static/src/img/banner.jpeg'],
    'license': 'AGPL-3',

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_view.xml',
    ],
}