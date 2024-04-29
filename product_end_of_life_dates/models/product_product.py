import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    end_of_life_announcement = fields.Date()
    end_of_life_support = fields.Date()
