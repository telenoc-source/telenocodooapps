

{
    'name': 'Tele Custom Product Labels',
    'version': '17.0.1.1.0',
    'category': 'Extra Tools',
    'author': 'Garazd Creation',
    'website': 'https://telenoc.org',
    'license': 'LGPL-3',
    'summary': 'Print custom product labels with barcode | Barcode Product Label',
    'images': ['static/description/banner.jpeg', 'static/description/icon.png'],
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/product_label_reports.xml',
        'report/product_label_templates.xml',
        'wizard/print_product_label_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': [
        'demo/product_demo.xml',
    ],
    'support': 'contact@telenoc.org',
    'application': True,
    'installable': True,
    'auto_install': False,
}
