{
    "name": "Product Information Management",
    "summary": """
        A simple key value model to store product informations.
    """,
    "author": "Mint System GmbH",
    "website": "https://github.com/Mint-system/",
    "category": "Inventory",
    "version": "18.0.1.0.0",
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
