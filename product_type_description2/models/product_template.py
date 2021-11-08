from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    type_description2 = fields.Char("Secondary Type Description")