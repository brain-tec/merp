# Copyright 2021 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

import math

from odoo import api,fields, models
from odoo.exceptions import UserError


class MultiplePackWizard(models.TransientModel):
    _name = 'multiple.pack.wizard'
    _description = 'Wizard: Multiple Packages'

    allowed_package_type_ids = fields.Many2many(
        'stock.package.type',
        compute='_compute_allowed_package_type_ids',
        readonly=True,
    )

    move_line_id = fields.Many2one(
        'stock.move.line',
        string="Move Line",
        required=True,
    )

    quantity_total = fields.Float(
        string="Total Quantity",
        readonly=True,
        help="Total quantity that must be packed.",
    )

    number_of_packages = fields.Integer(
        string="Number of packages",
        help="Fill either this field OR Items per package (only one).",
    )

    items_per_package = fields.Integer(
        string="Items per package",
        help="Fill either this field OR Number of packages (only one).",
    )

    package_type_id = fields.Many2one(
        'stock.package.type',
        string="Package Type",
    )

    @api.depends('move_line_id.move_id.picking_id.carrier_id')
    def _compute_allowed_package_type_ids(self):
        package_type_model = self.env['stock.package.type']
        for wizard in self:
            carrier = wizard.move_line_id.move_id.picking_id.carrier_id
            if carrier:
                allowed_ids = package_type_model.search([
                    ('package_carrier_type', '=', carrier.delivery_type),
                ]).ids
            else:
                allowed_ids = package_type_model.search([]).ids

            wizard.allowed_package_type_ids = [(6, 0, allowed_ids)]

    def action_pack(self):
        self.ensure_one()
        self._validate_inputs()
        self._create_packages()
        return {'type': 'ir.actions.act_window_close'}

    def _validate_inputs(self):
        self.ensure_one()

        qty = int(self.quantity_total or 0)
        if qty <= 0:
            raise UserError("Total quantity must be greater than zero.")

        has_n = bool(self.number_of_packages)
        has_items = bool(self.items_per_package)

        if has_n and has_items:
            raise UserError(
                "Must choose only one field: number_of_packages or items_per_package."
            )

        if not has_n and not has_items:
            raise UserError(
                "You must fill either number_of_packages or items_per_package."
            )

        if has_n and self.number_of_packages <= 0:
            raise UserError("Number of packages must be greater than zero.")

        if has_items and self.items_per_package <= 0:
            raise UserError("Items per package must be greater than zero.")

    def _get_package_quantities(self):
        self.ensure_one()

        qty = int(self.quantity_total)
        if self.number_of_packages:
            n = int(self.number_of_packages)

            # If user requests too many packages -> cap to qty (all ones)
            if n >= qty:
                return [1] * qty

            base = qty // n
            remainder = qty % n

            # Distribute +1 to first `remainder` packs (matches your examples)
            return [base + 1] * remainder + [base] * (n - remainder)

        # items_per_package path
        items = int(self.items_per_package)
        n = int(math.ceil(qty / float(items)))
        last = qty - items * (n - 1)
        return [items] * (n - 1) + [last]

    def _create_packages(self):
        self.ensure_one()
        move_line = self.move_line_id

        pack_quantities = self._get_package_quantities()
        packages = [self._create_single_package() for _ in range(len(pack_quantities))]

        # One package -> only assign destination package (do not change quantity)
        if len(pack_quantities) == 1:
            move_line.write({'result_package_id': packages[0].id})
            return

        # Multiple packages -> base line becomes first pack
        move_line.write({
            'result_package_id': packages[0].id,
            'qty_done': pack_quantities[0],
        })

        # Additional packs -> copy lines
        for i in range(1, len(pack_quantities)):
            self._create_line_for_package(move_line, packages[i], pack_quantities[i])

    def _create_single_package(self):
        vals = {}
        if self.package_type_id:
            vals['package_type_id'] = self.package_type_id.id
        return self.env['stock.quant.package'].create(vals)

    def _create_line_for_package(self, base_move_line, package, qty):
        base_move_line.copy({
            'result_package_id': package.id,
            'qty_done': qty,
        })
