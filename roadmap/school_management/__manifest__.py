# -*- coding: utf-8 -*-
{
    'name': 'School Management',
    'summary': 'School Management Demo',
    'description': """
    A Demo App For School Management
    """,
    'author': "Kai",
    'version': '1.0',
    'category': 'Basic',
    'depends': [
        'base','web'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml'
    ],
    'assets':{
        'web.assets_backend':[
            # 'school_management/static/src/**/*',
        ]
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}