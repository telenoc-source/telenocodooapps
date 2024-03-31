# -*- coding: utf-8 -*-
{
    'name': 'Tele Employee Documents',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': """Manages Employee Documents With Expiry Notifications.""",
    'description': 'Manages Employee Related Documents'
                   ' with Expiry Notifications.',
    'author': 'TeleNoc',
    'company': 'TeleNoc',
    'maintainer': 'TeleNoc',
    'website': "https://www.telenoc.org",
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/employee_checklist_data.xml',
        'data/ir_cron_data.xml',
        'views/employee_checklist_views.xml',
        'views/hr_employee_document_views.xml',
        'views/hr_employee_views.xml',
    ],
    'demo': ['data/data.xml'],
    'images': ['static/description/banner.jpeg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
