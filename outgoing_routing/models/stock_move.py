# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"
    _description = "Stock Move"

    ventor_picked = fields.Boolean('Ventor Picked')

    def write(self, vals):
        res = super().write(vals)

        if self.env.context.get("ventor_sync_ventor_picked"):
            return res

        if "ventor_picked" in vals:
            self.move_line_ids.with_context(ventor_sync_ventor_picked=True).write({
                "ventor_picked": vals["ventor_picked"],
            })

        return res
