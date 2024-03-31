# -*- coding: utf-8 -*-
{
    'name': 'Tele Export Product Stock in Excel',
    'version': '17.0.1.0.0',
    'summary': 'Advanced PDF & XLS reports for Product Stock.',
    'description': 'Advanced PDF & XLS reports for Product Stock by'
                   'corresponding warehouse and product categories.',
    'category': 'Warehouse',
    'author': 'TeleNoc',
    'company': 'TeleNoc',
    'maintainer': 'TeleNoc',
    'depends': [
        'sale_management',
        'stock',
        'purchase',
    ],
    'website': 'https://www.telenoc.org',
    'data': [
        'security/ir.model.access.csv',
        'wizard/stock_report_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'export_stockinfo_xls/static/src/js/action_manager.js',
        ],
    },
    'images': ['static/description/banner.jpeg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'auto_install': False,
}
