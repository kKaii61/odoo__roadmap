# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ClassManagement(models.Model):
    _name = "sm.class"
    _description = "Class Management"
    
    name = fields.Char("Class Name")
    class_type = fields.Char("Class Type")