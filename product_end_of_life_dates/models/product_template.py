import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    end_of_sale = fields.Date("EoS")
    end_of_life_announcement = fields.Date("EoL Announcement")
    end_of_life_support = fields.Date("EoL/S")
    # end_of_support = fields.Date("EoS")
    # end_of_life = fields.Date("EoL")
