from odoo import api, fields, models



class ProductProduct(models.Model):
    _inherit = "product.product"

    putaway_final_location_id = fields.Many2one(
        "stock.location",
        string="Final Putaway Location",
        compute="_compute_putaway_final_location",
        store=True,
    )

    putaway_final_locations_string = fields.Char(
        string="Putaway Rules Locations",
        compute="_compute_putaway_final_locations_string",
        readonly=True,
        store=False
    )

    @api.depends("categ_id")
    def _compute_putaway_final_location(self):
        for product in self:
            # product-specific rule
            rule = self.env["stock.putaway.rule"].search(
                [("product_id", "=", product.id)], limit=1
            )
            # product-category specific rule as fallback
            if not rule and product.categ_id:
                rule = self.env["stock.putaway.rule"].search(
                    [("category_id", "=", product.categ_id.id)], limit=1
                )
            product.putaway_final_location_id = rule.location_out_id if rule else False

    @api.depends("categ_id")
    def _compute_putaway_final_locations_string(self):
        for product in self:
            rules = self.env['stock.putaway.rule'].search([
                '|',
                ('product_id', '=', product.id),
                ('category_id', '=', product.categ_id.id)
            ])

            if not rules:
                product.putaway_final_locations_string = ""
                continue


            if len(rules) == 1:
                product.putaway_final_locations_string = rules[0].location_out_id.display_name if rules[0].location_out_id else "?"
            else:
                lines = []
                for rule in rules:
                    src = rule.location_in_id.display_name if rule.location_in_id else "?"
                    dst = rule.location_out_id.display_name if rule.location_out_id else "?"
                    lines.append(f"{src} → {dst}")

                product.putaway_final_locations_string = ", ".join(lines)
