from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    type_description = fields.Char()