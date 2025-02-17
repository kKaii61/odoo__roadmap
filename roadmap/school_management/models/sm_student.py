# -*- coding: utf-8 -*-
from odoo import api, fields, models

class StudentManagement(models.Model):
    _name = 'sm.student'
    _description = 'Student Management'

    name = fields.Char('Student\'s Name', required=True)
    age = fields.Integer("Student's Age", required=True)
    email = fields.Char("Student's Email")
    class_ids = fields.Many2many('sm.class','sm_class_student_relation','student_id','class_id',
                                 string="Class", ondelete="cascade", required=False)
    # Compute to get school name
    school_name = fields.Char(string="School Name", compute="_compute_school_name", store=True)
    # Compute to get class list
    class_list = fields.Char(string="Class list", compute="_compute_class_list", store=True)

    # create

    @api.model
    def create(self, vals):
        # Gọi phương thức gốc để tạo sinh viên
        student = super(StudentManagement, self).create(vals)

        # Gửi email sau khi tạo
        if student.email:
            student.auto_send_email()
        return student

    def btn_email_send(self):
        print(f"=========\nsend to {self.email} by button\n===========\n" if self.email else "\n===========\nNo email provided\n===============\n")
        mail_template = self.env.ref('school_management.student_confirm_email', raise_if_not_found=False)
        if mail_template:
            mail_template.sudo().send_mail(self.id, force_send=True)
        else:
            raise UserError("Template email not found!")
        
    def auto_send_email(self):
        mail_template = self.env.ref('school_management.student_confirm_email', raise_if_not_found=False)
        if mail_template:
            mail_template.sudo().send_mail(self.id, force_send=True)
        else:
            raise UserError("Template email not found!")

    # api
    @api.depends('class_ids.school_id', 'class_ids')
    def _compute_school_name(self):
        for student in self:
            schools = student.class_ids.mapped('school_id.name')  # Get school name from class_ids
            student.school_name = ', '.join(schools) if schools else "No school engaged"
    def _compute_class_list(self):
        for record in self:
            classes = record.class_ids
            record.class_list = classes.mapped('name') if classes else "No class registered"