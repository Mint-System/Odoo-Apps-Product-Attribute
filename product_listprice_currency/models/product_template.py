from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    list_price_eur = fields.Float("Sales Price EUR", default=1.0, digits="Product Price")
    list_price_usd = fields.Float("Sales Price USD", default=1.0, digits="Product Price")


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    base = fields.Selection(
        selection_add=[
            ("list_price_eur", "Sales Price EUR"),
            ("list_price_usd", "Sales Price USD"),
        ],
        ondelete={
            "list_price_eur": "set default",
            "list_price_usd": "set default",
        },
    )
