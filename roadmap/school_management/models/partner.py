from odoo import fields, models, api


class Partner(models.Model):
    _inherit = "res.partner"
    _description = "This add student fields"

    student_id = fields.Many2one("sm.student", string="StudentID")
    is_student = fields.Boolean("Student", default=False)

    @api.onchange("student_id")
    def _onchange_student_id(self):
        """Update the email when a student is linked to a partner."""
        if self.student_id:
            self.email = self.student_id.email
    @api.model
    def create(self, vals):
        """Ensure email is updated when creating partner from student."""
        if vals.get('student_id'):
            student = self.env['sm.student'].browse(vals['student_id'])
            vals['email'] = student.email
        return super(Partner, self).create(vals)

    def write(self, vals):
        """Ensure email is updated when updating partner from student."""
        if 'student_id' in vals:
            student = self.env['sm.student'].browse(vals['student_id'])
            vals['email'] = student.email
        return super(Partner, self).write(vals)