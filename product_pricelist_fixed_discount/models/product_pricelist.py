from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class ProductPricelistItem(models.Model):

    _inherit = 'product.pricelist.item'

    sequence = fields.Integer()