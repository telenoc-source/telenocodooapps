# -*- coding: utf-8 -*-
{
    'name': 'Tele Timesheet PDF Report',
    'version': '17.0.1.0.0',
    "category": "Project",
    'sequence': 25,
    'summary': 'Timesheet PDF Report of Employees',
    'description': 'Comprehensive timesheet PDF report summarizing employee '
                   'work hours and activities for efficient tracking and '
                   'management.',
    'author': 'TeleNoc',
    'company': 'TeleNoc',
    'maintainer': 'TeleNoc',
    'website': 'https://www.telenoc.org',
    'depends': ['hr', 'hr_timesheet'],
    'data': [
        'security/ir.model.access.csv',
        'report/timesheet_templates.xml',
        'report/timesheet_reports.xml',
        'wizard/timesheet_report_views.xml',
    ],
    'images': ['static/description/banner.jpeg'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
