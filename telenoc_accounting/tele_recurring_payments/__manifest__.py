# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Tele Odoo 17 Recurring Payment',
    'author': 'TeleNoc',
    'category': 'Accounting',
    'version': '1.0.0',
    'description': """Odoo 17 Recurring Payment, Recurring Payment In Odoo, Odoo 17 Accounting""",
    'summary': 'Use recurring payments to handle periodically repeated payments',
    'sequence': 11,
    'website': 'https://www.telenoc.org',
    'depends': ['account'],
    'license': 'LGPL-3',
    'data': [
        'data/sequence.xml',
        'data/recurring_cron.xml',
        'security/ir.model.access.csv',
        'views/recurring_template_view.xml',
        'views/recurring_payment_view.xml'
    ],
    'images': ['static/description/banner.jpeg'],
}
