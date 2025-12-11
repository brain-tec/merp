from odoo import SUPERUSER_ID, _, api


def migrate(cr, version):

    env = api.Environment(cr, SUPERUSER_ID, {})

    show_next_product_wave = env.ref("ventor_base.show_next_product_batch_picking", False)
    show_next_product_batch = env.ref("ventor_base.show_next_product_wave_picking", False)

    value = {
        "description": "Product field will show the next product to be picked. Use the setting during "
                       "picking and delivery. It is recommended to disable the setting for the reception area"
    }

    if show_next_product_wave:
        show_next_product_wave.write(value)
    if show_next_product_batch:
        show_next_product_batch.write(value)
