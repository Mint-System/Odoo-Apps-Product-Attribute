from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class ProductPackaging(models.Model):
    _inherit = 'product.packaging'

    parent_packaging = fields.Many2one('product.packaging', string='Parent Package')