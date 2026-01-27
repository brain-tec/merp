# Copyright 2026 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import api, models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    favorite_warehouse_id = fields.Many2one(
        comodel_name="stock.warehouse",
        string="Favorite Warehouse",
        help="Warehouse that will be used as user's preferred one in Ventor",
    )

    @api.onchange("allowed_warehouse_ids")
    def _onchange_allowed_warehouse_ids(self):
        if self.favorite_warehouse_id and self.favorite_warehouse_id not in self.allowed_warehouse_ids:
            self.favorite_warehouse_id = False
