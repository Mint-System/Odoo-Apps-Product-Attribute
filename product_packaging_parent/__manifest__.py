{
    "name": "Product Packaging Parent",
    "summary": """
        Define a parent packing for a product packging.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Inventory",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["product"],
    "data": ["views/product_packaging.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
    "qweb": ["static/src/xml/board.xml"],
}
