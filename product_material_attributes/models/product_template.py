import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    material_ids = fields.Many2many("product.material", string="Material")


class ProductMaterial(models.Model):
    _name = "product.material"
    _description = "Product Material"

    name = fields.Char(required=True)
    percent = fields.Char()

    @api.model
    def create(self, vals):
        name = vals.get("name")
        percent = vals.get("percent", False)
        materials = self.search([("name", "=", name), ("percent", "=", percent)])
        if materials:
            return materials[0]
        return super().create(vals)
