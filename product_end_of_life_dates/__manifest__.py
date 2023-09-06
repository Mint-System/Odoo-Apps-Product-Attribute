{
    "name": "Product End Of Life Dates",
    "summary": """
        Date fields for ens of support, sale and life.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Sales",
    "version": "15.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["stock"],
    "data": ["views/product_template.xml", "views/stock_quant.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
    "qweb": ["static/src/xml/board.xml"],
}
