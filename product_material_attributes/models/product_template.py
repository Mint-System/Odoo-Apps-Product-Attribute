import logging

from odoo import api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    material_ids = fields.Many2many("product.material", string="Material")


class ProductMaterial(models.Model):
    _name = "product.material"
    _description = "Product Material"

    name = fields.Char(required=True)
    percent = fields.Char()

    @api.constrains("name", "percent")
    def _check_name_percent_unique(self):
        for record in self:
            if (
                self.search_count(
                    [
                        ("name", "=", record.name),
                        ("percent", "=", record.percent),
                        ("id", "!=", record.id),  # Exclude current record
                    ]
                )
                > 0
            ):
                raise ValidationError(
                    'The combination of Name "%s" and Percent "%s" already exists!' % (record.name, record.percent)
                )
