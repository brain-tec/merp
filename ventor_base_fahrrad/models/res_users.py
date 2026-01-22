# Copyright 2026 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    favorite_operation_type = fields.Many2one(
        comodel_name="stock.picking.type",
        string="Favorite Operation Type",
        help="Operation type that will be used as user's preferred one in Ventor",
    )
