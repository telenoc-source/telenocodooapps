# -*- coding: utf-8 -*-

from odoo import fields, models


class TimesheetReport(models.TransientModel):
    """Create a Transient model for Wizard"""
    _name = 'timesheet.report'
    _description = 'Timesheet Report Wizard'

    user_id = fields.Many2one(
        'res.users',
        string="Employee",
        required=True, help="You can select the employee")
    from_date = fields.Date(
        string="Starting Date",
        help="You can select the starting dates for the PDF report")
    to_date = fields.Date(
        string="Ending Date",
        help="You can select the ending dates for the PDF report")

    def print_timesheet(self):
        """Redirects to the report with the values obtained from the wizard
        'data['form']': name of employee and the date duration"""
        data = {
            'employee': self.user_id.id,
            'start_date': self.from_date,
            'end_date': self.to_date,
        }
        return self.env.ref(
            'timesheets_by_employee.action_report_print_timesheets'). \
            report_action(self, data=data)
