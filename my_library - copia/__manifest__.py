# -*- coding: utf-8 -*-

{
    'name': "My library",
    'summary': "Manage books easily",
    'description': """
        Manage Library
        Description related to library.
    """,
    'author': "Giovanny Vizcaya",
    'website': "http://www.example.com",
    'category': 'Uncategorized',
    'version': '14.0.1',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book_view.xml'
    ],
    #'demo': ['demo.xml'],
}