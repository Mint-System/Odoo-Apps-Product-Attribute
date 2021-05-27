{
    'name': "Product Country of Origin",

    'summary': """
        Add field country of origin to the logistics tab.
    """,
    
    'author': 'Mint System GmbH, Odoo Community Association (OCA)',
    'website': 'https://www.mint-system.ch',
    'category': 'Manufacturing',
    'version': '14.0.1.0.0',
    'license': 'AGPL-3',
    
    'depends': ['stock'],

    'data': [
        'views/ir.model.fields.xml',
        'views/ir.ui.view.xml',
    ],

    'installable': True,
    'application': False,
}