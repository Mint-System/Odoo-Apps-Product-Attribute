{
    'name': "Product Type Description",

    'summary': """
        Add field type description to product.
    """,
    
    'author': 'Mint System GmbH, Odoo Community Association (OCA)',
    'website': 'https://www.mint-system.ch',
    'category': 'Manufacturing',
    'version': '14.0.1.0.0',
    'license': 'AGPL-3',
    
    'depends': ['stock'],

    'data': [
        'views/product_template.xml',
    ],

    'installable': True,
    'application': False,
}