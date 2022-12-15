# -*- coding: utf-8 -*-
{
    'name': "consult it - evaluation",
    'summary': "Implemente planes de evaluación y obtenga lo mejor de su fuerza laboral",
    'description': """
        Módulo de evaluaciones de desempeño de empleados
    """,
    'author': "Giovanny Vizcaya - Consult-It",
    'website': "https://consultit-as.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Generic Modules/Human Resources',
    'version': '14.0.1.0.3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'hr_appraisal', 'hr_employee_firstname', 'hr_employee_lastnames'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_appraisal_view.xml',
        'views/hr_appraisal_period_view.xml',
        'views/hr_appraisal_rem_act_view.xml',
        'views/hr_appraisal_competence_view.xml',
        'views/hr_appraisal_goal_view.xml',
        'views/res_company_view.xml',
        'views/hr_appraisal_note_tree_view.xml',
        'views/hr_appraisal_plan_view.xml',
        'views/hr_department_view.xml',
        'views/hr_job_family_view.xml',
        'report/report_example.xml',
        'report/report_example_template.xml'
        
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
