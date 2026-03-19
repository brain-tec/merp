# Copyright 2021 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields
from odoo.osv import expression


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    barcode_ids = fields.One2many(related='product_variant_ids.barcode_ids', readonly=False)

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        res = super().name_search(name=name, args=args, operator=operator, limit=limit)
        domain = args or []
        if name and not res:
            products = self.search_fetch(expression.AND([domain, [('barcode_ids.name', '=', name)]]), ['display_name'], limit=limit)
            return [(product.id, product.display_name) for product in products.sudo()]
        return res
