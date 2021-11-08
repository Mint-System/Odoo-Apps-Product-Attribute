from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    feeder_id = fields.Char()