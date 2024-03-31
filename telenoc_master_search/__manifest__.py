# -*- coding: utf-8 -*-

{
    'name': 'Tele Global Search',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """Easy Search in Customers, Products, Sale, Purchase, Inventory
    and Accounting modules""",
    'description': """Search, Global Search, Quick Search, Easy Search, Easy
    Search in Customers, Products, Sale, Purchase, Inventory and Accounting
    modules, Search, Advance search, global search """,
    'author': 'TeleNoc',
    'company': 'TeleNoc',
    'maintainer': 'TeleNoc',
    'website': 'https://www.telenoc.org',
    'depends': ['base', 'stock', 'sale', 'purchase'],
    'data': [
        'security/master_search_security.xml',
        'security/ir.model.access.csv',
        'views/master_search_view.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'master_search/static/src/scss/master_search.scss',
        ],
    },
    'images': ['static/description/banner.jpeg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
