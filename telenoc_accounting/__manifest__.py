# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Tele Odoo 17 Accounting',
    'version': '1.0.0',
    'category': 'Accounting',
    'summary': 'Accounting Reports, Asset Management and Account Budget, Recurring Payments, '
               'Lock Dates, Fiscal Year For Odoo 17 Community Edition, Accounting Dashboard, Financial Reports, '
               'Customer Follow up Management, Bank Statement Import, Odoo Budget',
    'description': 'Odoo 17 Financial Reports, Asset Management and '
                   'Account Budget, Financial Reports, Recurring Payments, '
                   'Bank Statement Import, Customer Follow Up Management,'
                   'Account Lock Date, Accounting Dashboard',
    'sequence': '1',
    'website': 'https://www.telenoc.org',
    'author': 'TeleNoc',
    'maintainer': 'TeleNoc',
    'license': 'LGPL-3',
    'support': 'contact@telenoc.org',
    'depends': [
        'accounting_pdf_reports',
        'om_account_asset',
        'om_account_budget',
        'om_fiscal_year',
        'om_recurring_payments',
        # 'om_account_bank_statement_import',
        'om_account_daily_reports',
        'om_account_followup',
    ],
    'demo': [],
    'data': [
        'security/group.xml',
        'views/menu.xml',
        'views/settings.xml',
        'views/account_group.xml',
        'views/account_tag.xml',
        'views/res_partner.xml',
        # 'views/account_coa_template.xml',
        'views/account_bank_statement.xml',
        'views/payment_method.xml',
        'views/reconciliation.xml',
        'views/account_journal.xml',
    ],
    'application': True,
    'images': ['static/description/banner.jpeg'],
}

