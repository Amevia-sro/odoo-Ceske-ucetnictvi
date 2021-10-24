from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    travel_service = fields.Boolean('Travel Service')
    used_goods = fields.Boolean('Used Goods')
