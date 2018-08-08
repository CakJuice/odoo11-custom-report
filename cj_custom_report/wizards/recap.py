# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class AttendanceRecapReportWizard(models.TransientModel):
    _name = 'attendance.recap.report.wizard'

    date_start = fields.Date(string="Start Date", required=True, default=fields.Date.today)
    date_end = fields.Date(string="End Date", required=True, default=fields.Date.today)

    @api.multi
    def get_report(self):
        """Call when button 'Get Report' clicked.
        """
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'date_start': self.date_start,
                'date_end': self.date_end,
            },
        }

        # use `module_name.report_id` as reference.
        # `report_action()` will call `get_report_values()` and pass `data` automatically.
        return self.env.ref('cj_custom_report.recap_report').report_action(self, data=data)


class ReportAttendanceRecap(models.AbstractModel):
    """Abstract Model for report template.

    for `_name` model, please use `report.` as prefix then add `module_name.report_name`.
    """

    _name = 'report.cj_custom_report.attendance_recap_report_view'

    @api.model
    def get_report_values(self, docids, data=None):
        date_start = datetime.strptime(data['form']['date_start'], DATE_FORMAT)
        date_end = datetime.strptime(data['form']['date_end'], DATE_FORMAT) + timedelta(days=1)
        date_diff = (date_end - date_start).days

        docs = []
        employees = self.env['hr.employee'].search([], order='name asc')
        for employee in employees:
            presence_count = self.env['hr.attendance'].search_count([
                ('employee_id', '=', employee.id),
                ('check_in', '>=', date_start.strftime(DATETIME_FORMAT)),
                ('check_out', '<', date_end.strftime(DATETIME_FORMAT)),
            ])

            absence_count = date_diff - presence_count

            docs.append({
                'employee': employee.name,
                'presence': presence_count,
                'absence': absence_count,
            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start.strftime(DATE_FORMAT),
            'date_end': (date_end - timedelta(days=1)).strftime(DATE_FORMAT),
            'docs': docs,
        }
