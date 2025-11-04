from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    putaway_final_location_id = fields.Many2one(
        "stock.location",
        string="Final Putaway Location",
        related="product_variant_ids.putaway_final_location_id",
        store=False,
        readonly=True,
    )

    putaway_final_locations_string = fields.Char(
        string="Putaway Rules Locations",
        related="product_variant_ids.putaway_final_locations_string",
        readonly=True
    )
