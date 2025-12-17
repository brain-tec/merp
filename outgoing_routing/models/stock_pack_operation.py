# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import fields, models, api


class StockPackOperation(models.Model):
    _inherit = 'stock.move.line'

    ventor_picked = fields.Boolean('Ventor Picked')

    @api.model
    def _compute_operation_valid(self):
        res = True
        if hasattr(super(StockPackOperation, self), '_compute_operation_valid'):
            res &= super(StockPackOperation, self)._compute_operation_valid()
        res &= not self.ventor_picked
        return res

    def write(self, vals):
        res = super().write(vals)

        if self.env.context.get("ventor_sync_ventor_picked"):
            return res

        if "ventor_picked" in vals and self.move_id:
            self.move_id.with_context(ventor_sync_ventor_picked=True).write({
                "ventor_picked": vals["ventor_picked"],
            })

        return res

