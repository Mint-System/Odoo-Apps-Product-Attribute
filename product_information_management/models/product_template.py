import logging
from odoo import fields, models, api, _
_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    attribute_ids = fields.Many2many('product.information.attribute', string='Product Information')
