# Copyright 2026 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).
from odoo import models


class ResUsersAllowedOperationTypeWizard(models.TransientModel):
    _inherit = "res.users.allowed.operation.type.wizard"

    def action_save(self):
        res = super().action_save()

        user = self.user_id
        if user.favorite_operation_type and user.favorite_operation_type not in user.allowed_operation_type_ids:
            user.favorite_operation_type = False

        return res
