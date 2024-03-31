# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Tele Cash Book, Day Book, Bank Book Financial Reports',
    'version': '17.0.1.0',
    'category': 'Invoicing Management',
    'summary': 'Cash Book, Day Book and Bank Book Report For Odoo 17',
    'description': 'Cash Book, Day Book and Bank Book Report For Odoo 17',
    'sequence': '10',
    'author': 'TeleNoc',
    'license': 'LGPL-3',
    'company': 'TeleNoc',
    'maintainer': 'TeleNoc',
    'support': 'contact@telenoc.org',
    'website': 'https://www.telenoc.org',
    'depends': ['account'],
    'live_test_url': '',
    'data': [
        'security/ir.model.access.csv',
        'views/om_daily_reports.xml',
        'wizard/daybook.xml',
        'wizard/cashbook.xml',
        'wizard/bankbook.xml',
        'report/reports.xml',
        'report/report_daybook.xml',
        'report/report_cashbook.xml',
        'report/report_bankbook.xml',
    ],
    'live_test_url': '',
    'images': ['static/description/banner.jpeg'],
}
