# -*- coding: utf-8 -*-
{
    "name": "School Management",
    "summary": "School Management Demo",
    "description": """
    A Demo App For School Management
    """,
    "author": "Kai",
    "version": "1.0",
    "category": "Basic",
    "depends": ["base", "web", "mail", "contacts"],
    "data": [
        "views/sm_school_views.xml",
        "views/sm_class_views.xml",
        "views/sm_student_views.xml",
        'views/partner_student_views.xml',
        "views/menus.xml",
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/cron.xml",
        "data/sm.school.csv",
        "data/sm.class.csv",
        "data/mail_template_data.xml",
        "reports/report_student.xml",
        "reports/report_student_templates.xml",
    ],
    "assets": {
        "web.assets_backend": [
            # 'school_management/static/src/**/*',
        ]
    },
    'bootstrap': True,
    "images": ["static/description/icon.png"],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
