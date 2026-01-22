# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

{
    'name': 'Ventor Base Fahrrad XXL',
    'version': '18.0.1.0.0',
    'author': 'VentorTech',
    'website': 'https://ventor.tech/',
    'license': 'LGPL-3',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'summary': 'Base module that allow relation between Ventor modules',
    'depends': [
        'ventor_base',
    ],
    'data': [
        'views/res_users.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'ventor_base/static/src/**/*',
        ],
    }
}
