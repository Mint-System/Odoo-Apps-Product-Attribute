import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    attribute_ids = fields.Many2many(
        "product.information.attribute",
        string="Product Information",
        compute="_compute_attribute_ids",
        inverse="_set_attribute_ids",
        store=True,
    )

    @api.depends("product_variant_ids", "product_variant_ids.attribute_ids")
    def _compute_attribute_ids(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.attribute_ids = template.product_variant_ids.attribute_ids
        for template in self - unique_variants:
            template.attribute_ids = []

    def _set_attribute_ids(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.attribute_ids = template.attribute_ids
            else:
                for product in template.product_variant_ids:
                    product.attribute_ids = product.attribute_ids + template.attribute_ids
