# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Trandom',
    'version': '0.1',
    'category': 'Hidden/Tests',
    'description': """ """,
    'depends': ['web', 'test_mail'],
    'data': [
        'security/libreria_security.xml',
        'security/ir.model.access.csv',
        'views/menu_view.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
