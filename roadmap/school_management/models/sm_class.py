# -*- coding: utf-8 -*-
from odoo import fields, models

class ClassManagement(models.Model):
    _name = "sm.class"
    _description = "Class Management"

    name = fields.Char("Class Name")
    class_type = fields.Char("Class Type")
    school_id = fields.Many2one('sm.school', string="School", ondelete="cascade")
    student_ids = fields.Many2many('sm.student', 'class_id', string="Students")