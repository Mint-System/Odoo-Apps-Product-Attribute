import logging
from odoo import fields, models, api, _
_logger = logging.getLogger(__name__)


class ProductInformationAttribute(models.Model):
    _name = 'product.information.attribute'
    _description = 'Product Information Attribute'
    _rec = 'key'

    key = fields.Char(required=True)
    attribute_type = fields.Selection([
        ('char', 'Char'),
        ('text', 'Text'),
        ('integer', 'Integer'),
        ('float', 'Float'),
        ('boolean', 'Boolean'),
    ], default='char', required=True)
    value_id = fields.Many2one('product.information.value', required=True, domain="[('attribute_type', '=', attribute_type)]")
    
    def get_value(self):
        options = {
            'char': self.value_id.char_value,
            'text': self.value_id.text_value,
            'integer': self.value_id.integer_value,
            'float': self.value_id.float_value,
            'boolean': self.value_id.boolean_value,
        }
        return options[self.attribute_type]

class ProductInformationValue(models.Model):
    _name = 'product.information.value'
    _description = 'Product Information Value'

    name = fields.Char('Value', compute='_compute_get_name', inverse='_inverse_set_name', store=True)
    attribute_ids = fields.One2many('product.information.attribute', 'value_id', required=True)
    attribute_type = fields.Char()

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
                'float': float(value.float_value),
                'boolean': bool(value.boolean_value),
            }
            value.name = options[value.attribute_id.attribute_type] if value.attribute_id else 'None'

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
                value.write({'boolean_value': bool(self.name) })