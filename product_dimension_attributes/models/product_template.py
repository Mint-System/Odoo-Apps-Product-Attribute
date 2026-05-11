import logging

from odoo import api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    dimension_ids = fields.Many2many("product.dimension", string="Dimension")


class ProductDimension(models.Model):
    _name = "product.dimension"
    _description = "Product Dimension"

    name = fields.Char(required=True)
    value = fields.Char()

    @api.constrains("name", "value")
    def _check_name_value_unique(self):
        for record in self:
            if (
                self.search_count(
                    [
                        ("name", "=", record.name),
                        ("value", "=", record.value),
                        ("id", "!=", record.id),  # Exclude current record
                    ]
                )
                > 0
            ):
                raise ValidationError(
                    'The combination of Name "%s" and Value "%s" already exists!' % (record.name, record.value)
                )
