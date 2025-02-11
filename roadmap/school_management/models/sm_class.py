# -*- coding: utf-8 -*-
from odoo import api,fields, models

class ClassManagement(models.Model):
    _name = "sm.class"
    _description = "Class Management"

    name = fields.Char("Class Name", required=True)
    class_type = fields.Char("Class Type", required=True)
    school_id = fields.Many2one('sm.school', string="School", ondelete="cascade", required=True)
    # fields.Many2many( comodel_name=comodel_name, relation=relation, column1=column1, column2=column2, string=string)
    student_ids = fields.Many2many('sm.student', 'sm_class_student_relation','class_id','student_id',string="Students")

    total_students = fields.Integer("Total Students", compute="_compute_student_data", store=True)
    avg_age = fields.Integer("Average Age", compute="_compute_student_data", store=True)

    
    @api.depends('student_ids', 'student_ids.age')
    def _compute_student_data(self):
        for record in self:
            students = record.student_ids
            record.total_students = len(students)
            record.avg_age = sum(students.mapped('age')) / len(students) if students else 0