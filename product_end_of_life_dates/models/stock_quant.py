import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    end_of_support = fields.Date(related='product_id.end_of_support')
    end_of_sale = fields.Date(related='product_id.end_of_sale')
    end_of_life = fields.Date(related='product_id.end_of_life')