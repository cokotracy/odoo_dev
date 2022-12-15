# -*- coding: utf-8 -*-
# Powered by Cereza Technology.
# © 2022 Cereza Technology. (<https://cerezatechnology.com/>)

{
    'name': "partner_pet",
    'version': '15.0.1.0',
   'summary': "Customer pet data information",
    'description': """
        This module adds customers pet data information.
    """,
    'author': "Ing. Giovanny Vizcaya",
    'website': "https://cerezatechnology.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/res_partner_view_inherit.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
