# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Ws_Order(models.Model):
    _inherit = "sale.order"

    def generate_sale_report(self):
        return self.env.ref("ws_order.action_sale_order_report_pdf").report_action(self)
