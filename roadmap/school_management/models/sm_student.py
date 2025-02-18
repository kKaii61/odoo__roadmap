# -*- coding: utf-8 -*-
from odoo import api, fields, models

# utils
from datetime import date, timedelta


class StudentManagement(models.Model):
    _name = "sm.student"
    _description = "Student Management"

    name = fields.Char("Student's Name", required=True)
    age = fields.Integer("Student's Age", required=True)
    email = fields.Char("Student's Email")
    # partner_ids = fields.One2many('res.partner', 'email', string='partner')

    join_date = fields.Date(
        "Join Date",
        default=fields.Date.context_today,  # Current date
        required=True,
    )
    graduated_date = fields.Date(
        "Graduated Date",
        # compute="_compute_graduated_date",  # join_date + 4years  // Comment this line to test cronjob
        store=True,
    )
    status = fields.Selection(
        [
            ("studying", "Currently Studying"),
            ("graduated", "Graduated"),
            ("dropped", "Dropped Out"),
            ("suspended", "Suspended"),
        ],
        string="Status",
        compute="_compute_status",
        store=True,
        default="studying",  # "Currently Studying"
    )

    class_ids = fields.Many2many(
        "sm.class",
        "sm_class_student_relation",
        "student_id",
        "class_id",
        string="Class",
        ondelete="cascade",
        required=False,
    )
    # Compute to get school name
    school_name = fields.Char(
        string="School Name", compute="_compute_school_name", store=True
    )
    # Compute to get class list
    class_list = fields.Char(
        string="Class list", compute="_compute_class_list", store=True
    )

    # ====================== MODEL =========================
    #
    #
    @api.model
    def create(self, vals):
        # Gọi phương thức gốc để tạo sinh viên
        student = super(StudentManagement, self).create(vals)

        # Send Email After Create
        if student.email:
            student.auto_send_email()
        return student

    #
    #
    # ============================================================================

    # ====================== METHODS =========================
    #
    #
    def btn_email_send(self):
        print(
            f"=========\nsend to {self.email} by button\n===========\n"
            if self.email
            else "\n===========\nNo email provided\n===============\n"
        )
        mail_template = self.env.ref(
            "school_management.student_confirm_email", raise_if_not_found=False
        )
        if mail_template:
            try:
                mail_template.sudo().send_mail(self.id, force_send=True)
            except Exception as e:
                raise e
        else:
            raise UserError("Template email not found!")

    def auto_send_email(self):
        mail_template = self.env.ref(
            "school_management.student_confirm_email", raise_if_not_found=False
        )
        if mail_template:
            try:
                mail_template.sudo().send_mail(self.id, force_send=True)
            except Exception as e:
                raise e
        else:
            raise UserError("Template email not found!")

    def update_student_status(self):
        """Scheduled cron job to update student statuses based on graduation date"""
        today = date.today()
        print("\n=====================\nCalled Update Student\n===================\n")
        students = self.search(
            [("graduated_date", "<=", today), ("status", "=", "studying")]
        )
        for student in students:
            student.status = "graduated"

    #
    #
    # ============================================================================

    # ====================== API =========================
    #
    #
    @api.depends("class_ids.school_id", "class_ids")
    def _compute_school_name(self):
        for student in self:
            schools = student.class_ids.mapped(
                "school_id.name"
            )  # Get school name from class_ids
            student.school_name = ", ".join(schools) if schools else "No school engaged"

    def _compute_class_list(self):
        for record in self:
            classes = record.class_ids
            record.class_list = (
                classes.mapped("name") if classes else "No class registered"
            )

    # Compute graduated date
    @api.depends("join_date")
    def _compute_graduated_date(self):
        for student in self:
            if student.join_date:
                student.graduated_date = student.join_date + timedelta(days=4 * 365)
            else:
                student.graduated_date = None

    # Compute status
    @api.depends("graduated_date")
    def _compute_status(self):
        today = date.today()
        for student in self:
            if student.graduated_date and student.graduated_date <= today:
                student.status = "graduated"
            elif student.status not in [
                "dropped",
                "suspended",
            ]:  # Not change if 'dropped' or 'suspended'
                student.status = "studying"

    # @api.onchange('partner_ids')
    # def _onchange_student_id(self):
    #     """Update the email when a student is linked to a partner."""
    #     if self.student_id:
    #         self.email = self.partner_ids.email
    #
    #
    # ============================================================================
