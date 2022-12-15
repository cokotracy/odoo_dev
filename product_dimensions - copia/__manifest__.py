# -*- coding: utf-8 -*-
# Copyright 2022 Cereza Technology  (https://cerezatechnology.com/)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "product_dimensions",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Giovanny Vizcaya",
    'website': "https://cerezatechnology.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product',
    'version': '15.1.0',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_view.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
