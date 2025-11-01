import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    dimension_ids = fields.Many2many("product.dimension", string="Dimension")


class ProductDimension(models.Model):
    _name = "product.dimension"
    _description = "Product Dimension"

    name = fields.Char(required=True)
    value = fields.Char()

    @api.model
    def create(self, vals):
        name = vals.get("name")
        value = vals.get("value", False)
        dimensions = self.search([("name", "=", name), ("value", "=", value)])
        if dimensions:
            return dimensions[0]
        return super().create(vals)
