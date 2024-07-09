from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    type_description2 = fields.Char("Secondary Type Description")
