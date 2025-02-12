# -*- coding: utf-8 -*-
from odoo import api, fields, models

class StudentManagement(models.Model):
    _name = 'sm.student'
    _description = 'Student Management'

    name = fields.Char('Student Name', required=True)
    age = fields.Integer("Student Age", required=True)
    class_ids = fields.Many2many('sm.class','sm_class_student_relation','student_id','class_id',
                                 string="Class", ondelete="cascade", required=False)
    # Compute to get school name
    school_name = fields.Char(string="School Name", compute="_compute_school_name", store=True)
    
    @api.depends('class_ids.school_id')
    def _compute_school_name(self):
        for student in self:
            schools = student.class_ids.mapped('school_id.name')  # Lấy danh sách tên trường từ class_ids
            student.school_name = ', '.join(schools) if schools else "No School"