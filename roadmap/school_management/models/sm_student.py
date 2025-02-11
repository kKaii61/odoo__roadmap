# -*- coding: utf-8 -*-
from odoo import fields, models

class StudentManagement(models.Model):
    _name = 'sm.student'
    _description = 'Student Management'

    name = fields.Char('Student Name', required=True)
    age = fields.Integer("Student Age", required=True)
    class_ids = fields.Many2many('sm.class', string="Class", ondelete="cascade", required=False)
