{
    "name": "Product Information Management",
    "summary": """
        A simple key value model to store product informations.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Inventory",
    "version": "16.0.1.3.0",
    "license": "AGPL-3",
    "depends": ["product", "sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_template.xml",
        "views/product_information_attribute.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
