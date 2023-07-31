import logging, ast
from odoo import fields, models, api, _
_logger = logging.getLogger(__name__)
from odoo.exceptions import UserError


class ProductInformationAttribute(models.Model):
    _name = 'product.information.attribute'
    _description = 'Product Information Attribute'
    _rec = 'key_id'

    key_id = fields.Many2one('product.information.key', required=True)
    attribute_type = fields.Selection([
        ('char', 'Char'),
        ('text', 'Text'),
        ('integer', 'Integer'),
        ('float', 'Float'),
        ('boolean', 'Boolean'),
    ], default='char', required=True)
    value_id = fields.Many2one('product.information.value', domain="[('attribute_type', '=', attribute_type)]")
    
    @api.onchange('attribute_type')
    def _onchange_attribute_type(self):
        if self.value_id:
            # raise UserError(_('Remove value before changing the attribute type.'))
            warning = {
                'title': _('Warning'),
                'message': _('Remove value before changing the attribute type.')
            }
            return {'warning': warning}

    _sql_constraints = [
        ('key_value_unique', 'unique(key_id,valude_id)', "Key and value combination must be unique.")
    ]

class ProductInformationKey(models.Model):
    _name = 'product.information.key'
    _description = 'Product Information Key'

    name = fields.Char('Key', store=True)

    _sql_constraints = [
        ('name_unique', 'unique(name)', "Key must be unique.")
    ]

class ProductInformationValue(models.Model):
    _name = 'product.information.value'
    _description = 'Product Information Value'

    name = fields.Char('Value', compute='_compute_get_name', inverse='_inverse_set_name')
    attribute_ids = fields.One2many('product.information.attribute', 'value_id', required=True)
    attribute_type = fields.Char(required=True)

    char_value = fields.Char(readonly=True)
    text_value = fields.Text(readonly=True)
    integer_value = fields.Integer(readonly=True)
    float_value = fields.Float(readonly=True)
    boolean_value = fields.Boolean(readonly=True)

    def _compute_get_name(self):
        for value in self:
            options = {
                'char': value.char_value,
                'text': value.text_value,
                'integer': str(value.integer_value),
                'float': str(value.float_value),
                'boolean': str(value.boolean_value),
            }
            value.name = options[value.attribute_type]

    @api.depends('char_value', 'text_value', 'integer_value')
    def _inverse_set_name(self):
        for value in self:
            attribute_type = value.attribute_type # self._context['default_attribute_type']
            if attribute_type == 'char':
                value.write({'char_value': self.name })
            if attribute_type == 'text':
                value.write({'text_value': self.name })
            if attribute_type == 'integer':
                value.write({'integer_value': int(self.name) })
            if attribute_type == 'float':
                value.write({'float_value': float(self.name) })
            if attribute_type == 'boolean':
                value.write({'boolean_value': ast.literal_eval(self.name) })