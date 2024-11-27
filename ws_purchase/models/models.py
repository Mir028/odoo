# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Ws_purchase(models.Model):
    _inherit = "purchase.order"

    order_priority = fields.Selection(
        [("low", "Low"), ("medium", "Medium"), ("high", "High")], string="Priority"
    )

    def generate_purchase_order_report(self):
        order_lines = self.order_line
        total_qty = sum(order_lines.mapped("product_qty"))
        total_cost = self.amount_total

        return {
            "type": "ir.actions.act_window",
            "name": "Purchase Order Report",
            "view_mode": "form",
            "res_model": "purchase.order.report.wizard",
            "target": "new",
            "context": {
                "default_purchase_id": self.id,
                "default_total_qty": total_qty,
                "default_total_cost": total_cost,
            },
        }


class PurchaseOrderReportWizard(models.TransientModel):
    _name = "purchase.order.report.wizard"
    _description = "Purchase Order Report Wizard"

    purchase_id = fields.Many2one("purchase.order", string="Purchase Order")
    total_qty = fields.Float(string="Total Quantity Purchased")
    total_cost = fields.Float(string="Total Cost")

    def generate_pdf_report(self):
        return self.env.ref(
            "module_name.action_purchase_order_report_pdf"
        ).report_action(self)
