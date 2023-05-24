from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    description_purchase = fields.Text(
        'Purchase Description', translate=True)
    description_sale = fields.Text(
        'Sales Description', translate=True,
        help="A description of the Product that you want to communicate to your customers. "
             "This description will be copied to every Sales Order, Delivery Order and Customer Invoice/Credit Note")
    description_picking = fields.Text('Description on Picking', translate=True)
    description_pickingout = fields.Text('Description on Delivery Orders', translate=True)
    description_pickingin = fields.Text('Description on Receptions', translate=True)

    def get_product_multiline_description_sale(self):
        name = super().get_product_multiline_description_sale()        
        if not self.description_sale and self.product_tmpl_id.description_sale:
            if self.user_has_groups('sale_order_line_description.group_use_product_description_per_so_line'):
                name = self.product_tmpl_id.description_sale
            else:
                name = self.display_name
                name += '\n' + self.product_tmpl_id.description_sale
        return name