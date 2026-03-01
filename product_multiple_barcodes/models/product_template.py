# Copyright 2021 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields
from odoo.fields import Domain


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    barcode_ids = fields.One2many(related='product_variant_ids.barcode_ids', readonly=False)

    @api.model
    def name_search(self, name='', domain=None, operator='ilike', limit=100):
        res = super().name_search(name=name, domain=domain, operator=operator, limit=limit)
        domain = Domain(domain or Domain.TRUE)
        if not res:
            products = self.search_fetch(domain & Domain('barcode_ids.name', '=', name), ['display_name'], limit=limit)
            return [(product.id, product.display_name) for product in products.sudo()]
        return res
