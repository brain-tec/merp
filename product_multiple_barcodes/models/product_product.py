# Copyright 2021 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.fields import Domain
from odoo.exceptions import UserError


class ProductProduct(models.Model):
    _inherit = 'product.product'

    barcode_ids = fields.One2many(
        'product.barcode.multi',
        'product_id',
        string='Additional Barcodes',
    )

    _barcode_uniq = models.Constraint("CHECK (1=1)", "No error")

    @api.model
    def name_search(self, name='', domain=None, operator='ilike', limit=100):
        res = super().name_search(name=name, domain=domain, operator=operator, limit=limit)
        domain = Domain(domain or Domain.TRUE)
        if not res:
            products = self.search_fetch(domain & Domain('barcode_ids.name', '=', name), ['display_name'], limit=limit)
            return [(product.id, product.display_name) for product in products.sudo()]
        return res

    @api.constrains('barcode', 'barcode_ids', 'active')
    def _check_unique_barcode(self):
        barcodes_duplicate = []
        for product in self:
            barcode_names = []
            if product.barcode_ids:
                barcode_names = product.mapped('barcode_ids.name')
            if product.barcode:
                barcode_names.append(product.barcode)
            if not barcode_names:
                continue
            products = self.env['product.product'].search([
                ('barcode', 'in', barcode_names),
                ('id', '!=', product.id),
                ('active', '=', True),
            ])
            barcode_ids = self.env['product.barcode.multi'].search([
                ('name', 'in', barcode_names),
                ('product_id', '!=', product.id),
                ('product_id.active', '=', True),
            ])
            if len(barcode_names) != len(set(barcode_names)):
                barcodes_multi = set([barcode for barcode in barcode_names if barcode_names.count(barcode) > 1])
                for barcode in barcodes_multi:
                    barcodes_duplicate.append(barcode)
            if barcode_ids:
                barcodes = [barcode.name for barcode in barcode_ids]
                for barcode in barcodes:
                    barcodes_duplicate.append(barcode)
            if products:
                barcodes_product = [product.barcode for product in products]
                for barcode in barcodes_product:
                    barcodes_duplicate.append(barcode)
        if barcodes_duplicate:
            raise UserError(
                _(
                    "The following barcode(s): {0} was found in other active products."
                    "\nNote that product barcodes should not repeat themselves both in "
                    '"Barcode" field and "Additional Barcodes" field.'
                ).format(", ".join(set(barcodes_duplicate)))
            )
