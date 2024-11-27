# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class JobQueue(models.Model):
    _inherit = "queue.job"

    products = fields.One2many("product.template", "job_id", string="Products")

    @api.model
    def create(self, vals):
        product_name = self.env.context.get("product_name", "Job has no product")
        vals["name"] = product_name
        vals["model_name"] = "Product Template"

        return super(JobQueue, self).create(vals)


class ProductTemplate(models.Model):
    _inherit = "product.template"
    job_id = fields.Many2one(
        "queue.job", string="Job Queue", help="Job linked to this product"
    )

    def generate_report_order(self):
        for product in self:
            data = {
                "name": product.name,
                "description_sale": product.description_sale,
                "product_price": product.list_price,
                "product_tax": product.taxes_id,
            }

            return {
                "type": "ir.actions.report",
                "report_name": "joby.report_product",
                "report_type": "qweb-pdf",
                "dates": data,
                "context": {"product_id": product.id},
            }

    def button_update_stuff(self):
        tax = self.tax_19()
        supplier = [(4, tax.id)]

        self = self.with_context(product_name=self.name)

        update = f"{self.name} Updated "

        values = {
            "name": update + str(fields.Datetime.now()),
            "description_sale": "This is the description after the job "
            + str(fields.Datetime.now()),
            "list_price": 10.1,
            "taxes_id": supplier,
        }

        self.with_delay().update_product_details(values)

    def tax_19(self):
        # Searching for the 19% tax in account.tax
        tax = self.env["account.tax"].search([("name", "=", "19%")], limit=1)
        if not tax:
            # Creating a tax group if it doesn t exist
            tax_group = self.env["account.tax.group"].search(
                [("name", "=", "General Sales Taxes")], limit=1
            )
            if not tax_group:
                tax_group = self.env["account.tax.group"].create(
                    {
                        "name": "General Sales Taxes",
                    }
                )
            tax = self.env["account.tax"].create(
                {
                    "name": "19%",
                    "amount": 19.0,
                    "type_tax_use": "sale",
                    "tax_group_id": tax_group.id,
                    "amount_type": "percent",
                }
            )

        return tax

    def update_product_details(self, values):
        if not isinstance(values, dict):
            raise ValidationError("Value is incorrect")
        self.write(values)
        print(f"I am updating this product{self.name}")
        return


class Joby(models.Model):
    _name = "joby.joby"
    _description = "joby.joby"

    name = fields.Char(string="Name")
    sale_description = fields.Char(string="Sale Description")
    sale_price = fields.Float(string="Sale Price")
    tex = fields.Char(string="Tex")
