from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    feeder_id = fields.Char()
