import logging
from odoo import models, fields
_logger = logging.getLogger(__name__)


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    x_default_code = fields.Char()
    x_hostname = fields.Char()
    x_forcepoint_pos = fields.Char()
    x_forcepoint_pol = fields.Char()
    x_location = fields.Char()
    x_managed_service = fields.Selection([
        ('high', 'MS1 High'),
        ('medium', 'MS1 Medium'),
        ('low', 'MS1 Low'),
        ('central', 'MS1 Central')
    ])
