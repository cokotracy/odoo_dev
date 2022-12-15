# -*- coding: utf-8 -*-
{
    'name': "Consult-IT Inventario",

    'summary': """
        Módulo avanzado de Inventario
        """,
    'description': """
        Módulo avanzado de Inventario con funcionalidades extras.
    """,
    'author': "Ing. Giovanny Vizcaya - Consult-IT",
    'website': "https://consultit-as.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory/Inventory',
    'version': '14.0.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'fleet', 'stock', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/stock_cargo_entry_control_view.xml',
        'views/stock_cargo_output_control_view.xml',
        'views/stock_fleet_container_view.xml',
        'views/stock_dua_view.xml',
        'views/stock_batch_view.xml',
        'views/stock_picking_view.xml',
        'views/stock_scrap_view.xml',
        'report/stock_scrap_report.xml',
        'report/stock_scrap_report_template.xml',
        'report/stock_checklist_report.xml',
        'report/stock_checklist_report_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
