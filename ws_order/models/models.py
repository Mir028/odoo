# -*- coding: utf-8 -*-
import base64
import io
import xlsxwriter

from odoo import models, fields, api


class Ws_Order(models.Model):
    _inherit = "sale.order"

    def generate_sale_report(self):
        return self.env.ref("ws_order.action_sale_order_report_pdf").report_action(self)

    def generate_sale_report_excel(self):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet("Sale Report Excel")

        header = ["Order", "Customer", "Order Date", "Total"]
        worksheet.write_row(0, 3, header)

        row = 1
        for order in self:
            worksheet.write_row(row, 0, order.name)
            worksheet.write_row(row, 1, order.partner_id.name)
            worksheet.write_row(row, 2, order.date_order.strftime("%m/%d/%Y"))
            worksheet.write_row(
                row,
                0,
                [
                    order.name,
                    order.partner_id.name,
                    order.date_order.strftime("%Y-%m-%d") if order.date_order else "",
                    order.amount_total,
                ],
            )

            row += 1

        workbook.close()
        output.seek(0)

        attachment = self.env["ir.attachment"].create(
            {
                "name": f"{self.name}.xlsx",
                "type": "binary",
                "datas": base64.b64encode(output.getvalue()),
                "res_model": "sale.order",
                "res_id": self.id,
            }
        )

        # Return the file as a downloadable URL
        return {
            "type": "ir.actions.act_url",
            "url": f"/web/content/{attachment.id}?download=true",
            "target": "new",
        }
