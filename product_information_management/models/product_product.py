import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = "product.product"

    attribute_ids = fields.Many2many("product.information.attribute", string="Product Information")

    def get_value_by_key(self, key):
        self.ensure_one()

        attribute = self.attribute_ids.filtered(lambda a: a.key_id.name == key)[:1]
        if attribute:
            options = {
                "char": attribute.value_id.char_value,
                "text": attribute.value_id.text_value,
                "integer": attribute.value_id.integer_value,
                "float": attribute.value_id.float_value,
                "boolean": attribute.value_id.boolean_value,
            }
            return options[attribute.attribute_type]
        else:
            return None
