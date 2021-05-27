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
    
    'depends': ['base'],

    'data': [
        'views/ir.ui.view.xml',
        'views/ir.model.fields.xml',
    ],

    'installable': True,
    'application': False,
}