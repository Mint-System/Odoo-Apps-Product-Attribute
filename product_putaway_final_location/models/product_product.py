from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = "product.product"

    putaway_final_location_id = fields.Many2one(
        "stock.location",
        string="Final Putaway Location",
        compute="_compute_putaway_final_location",
        store=False,
    )

    @api.depends('categ_id')
    def _compute_putaway_final_location(self):
        for product in self:
            # product-specific rule
            rule = self.env['stock.putaway.rule'].search([('product_id', '=', product.id)], limit=1)
            # product-category specific rule as fallback
            if not rule and product.categ_id:
                rule = self.env['stock.putaway.rule'].search([('category_id', '=', product.categ_id.id)], limit=1)
            product.putaway_final_location_id = rule.location_out_id if rule else False
