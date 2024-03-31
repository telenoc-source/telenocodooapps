# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Tele Sale Order Automation',
    'version' : '1.0',
    'author':'TeleNoc',
    'category': 'Sales',
    'maintainer': 'TeleNoc',
    'summary': """Enable auto sale workflow with sale order confirmation. Include operations like Auto Create Invoice, Auto Validate Invoice and Auto Transfer Delivery Order.""",
    'description': """

        You can directly create invoice and set done to delivery order by single click

    """,
    'website': 'https://www.telenoc.org',
    'license': 'LGPL-3',
    'support':'contact@telenoc.com',
    'depends' : ['sale_stock'],
    'data': [
        'views/stock_warehouse.xml',
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.jpeg'],

}
