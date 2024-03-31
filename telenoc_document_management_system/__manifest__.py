# -*- coding: utf-8 -*-
{
    'license': 'LGPL-3',
    'name': "Tele Document Management System",
    'summary': "Enterprise online document management",
    'author': "renjie TeleNoc",
    'website': "https://renjie.me",
    'support': 'i@renjie.me',
    'category': 'Document Management',
    'version': '1.0',
    'depends': ['mail'],
    'data': [
        'security/account_security.xml',
        'security/ir.model.access.csv',
        'views/document.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}