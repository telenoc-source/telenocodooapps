{
        'name': 'Tele PostgreSQL Query Deluxe',
        'description': 'Execute postgreSQL query into Odoo interface',
        'author': 'TeleNoc',
        'depends': ['base', 'mail'],
        'application': True,
        'version': '17.0.0.3',
        'license': 'AGPL-3',
        'support': 'contact@telenoc.org',
        'website': '',
        'installable': True,

        'data': [
            'security/security.xml',
            'security/ir.model.access.csv',

            'views/querydeluxe.xml',

            'wizard/pdforientation.xml',

            'report/print_pdf.xml',

            'datas/data.xml'
            ],

        'images': ['static/description/banner.jpeg']
}

