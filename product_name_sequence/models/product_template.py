# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Set default name to New
    name = fields.Char('Name', index=True, required=True, translate=True, default=lambda self: _('New'))

    _sql_constraints = [
        ('name_unique', 'unique (name)', "Product with the same name already exists."),
    ]

    @api.model
    def create(self, vals):
        # Check if name is set to default value
        if vals.get('name', _('New')) == _('New'):
            # Generate name from sequence
            vals['name'] = self.env['ir.sequence'].next_by_code('product.template')
        
        # Call parent create method
        return super(ProductTemplate, self).create(vals)
    
    @api.model
    def write(self, vals):
        # Check if name is set to default value
        if 'name' in vals and vals.get('name', _('New')) == _('New'):
            # Generate name from sequence
            vals['name'] = self.env['ir.sequence'].next_by_code('product.template')

        # Call parent write method
        return super(ProductTemplate, self).write(vals)