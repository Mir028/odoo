# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class Ws_Invoice(models.Model):
    _inherit = "account.move"

    def action_send_overdue_invoice(self):
        for invoice in self:
            if (
                invoice.invoice_date_due
                and invoice.invoice_date_due < fields.Datetime.today()
                and invoice.state == "posted"
            ):
                if not invoice.partner_id.email:
                    raise UserError("The customer does not have an email address")

                mail_template = self.env.ref("account.email_template_edi_invoice")
                if not mail_template:
                    raise UserError("Email template is missing")

                mail_template.send_mail(invoice.id, force_send=True)
                invoice.message_post(body="Overdue reminder sent to the customer.")

            else:
                raise UserError("Invoice state is invalid")
