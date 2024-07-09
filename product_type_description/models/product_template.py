from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    type_description = fields.Char()
