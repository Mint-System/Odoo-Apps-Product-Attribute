# -*- coding: utf-8 -*-
{
    'name': "Product Name Sequence",

    'summary': """
        Generate product name from sequence.
    """,

    'description': """
        Generate product name from sequence.
        Generate name only if name field is not edited manually.
        Ensure that product name is unique.
    """,

    'author': "Mint System GmbH",
    'website': "https://www.mint-system.ch",
    'category': 'Manufacturing',
    'version': '14.0.1.0.0',

    'depends': ['product'],

    'data': [
        'data/ir_sequence_data.xml',
    ],

    'installable': True,
    'application': False,
}