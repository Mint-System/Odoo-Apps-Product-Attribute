# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class ProductCategory(models.Model):
    # _name = "product.category"
    # _inherit = ["product.category"]
    _inherit = "product.category"

    tracking = fields.Selection(
        selection=[("none", "None"), ("serial", "Serial"), ("lot", "Lot")],
        default="none",
    )
