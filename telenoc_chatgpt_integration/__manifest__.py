# -*- coding: utf-8 -*-
# Copyright (c) 2020-Present InTechual Solutions. (<https://intechualsolutions.com/>)

{
    'name': 'Tele Odoo ChatGPT Integration',
    'version': '1.0.0',
    'license': 'AGPL-3',
    'summary': 'Odoo ChatGPT Integration',
    'description': 'Allows the application to leverage the capabilities of the GPT language model to generate human-like responses, providing a more natural and intuitive user experience',
    'author': 'TeleNoc',
    'company': 'TeleNoc',
    'maintainer': 'TeleNoc',
    'website': 'https://telenoc.org',
    'depends': ['base', 'base_setup', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/chatgpt_model_data.xml',
        'data/mail_channel_data.xml',
        'data/user_partner_data.xml',
        'views/res_config_settings_views.xml',
    ],
    'external_dependencies': {'python': ['openai']},
    'images': ['static/description/banner.jpeg'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
