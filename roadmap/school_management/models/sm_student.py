# -*- coding: utf-8 -*-
from odoo import fields, models

class StudentManagement(models.Model):
    _name = 'sm.student'
    _description = 'Student Management'

    name = fields.Char('Student Name')
    age = fields.Integer("Student Age")
    classroom = fields.Char("Class Register")