# -*- coding: utf-8 -*-
from odoo import fields, models

class SchoolManagement(models.Model):
    _name = 'sm.school'
    _description = 'School Management'

    name = fields.Char('School Name')