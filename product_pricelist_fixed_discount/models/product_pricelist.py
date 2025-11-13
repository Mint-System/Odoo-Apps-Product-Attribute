import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ProductPricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    sequence = fields.Integer()
