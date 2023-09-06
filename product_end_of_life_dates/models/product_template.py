import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    end_of_support = fields.Date()
    end_of_sale = fields.Date()
    end_of_life = fields.Date()