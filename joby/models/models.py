# -*- coding: utf-8 -*-
from itertools import product

from attr.validators import instance_of
from odoo import models, fields, api
from odoo.addons.test_convert.tests.test_env import field
from odoo.exceptions import ValidationError
from odoo.release import product_name


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def button_do_stuff(self):
        tax = self.tax_19()
        supplier = [(4, tax.id)]

        product = self.env['product.template'].browse(self.id)
        update = f"{product.name} Updated "

        values = {"name": update + str(fields.Datetime.now()),
                  "description_sale" : "This is the description after the job " + str(fields.Datetime.now()),
                  "list_price": 10.1,
                  "taxes_id": supplier,
                  "supplier_taxes_id": supplier,
                  }

        self.with_delay().update_product_details(values)

    def tax_19(self):
        #Searching for the 19% tax in account.tax
        tax = self.env['account.tax'].search([('name', '=', '19%')], limit=1)
        if not tax:
            #Creating a tax group if it doesn t exist
            tax_group = self.env['account.tax.group'].search([('name', '=', 'General Sales Taxes')], limit=1)
            if not tax_group:
                tax_group = self.env['account.tax.group'].create({
                    'name': 'General Sales Taxes',
                })
            tax = self.env['account.tax'].create({
                'name': '19%',
                'amount': 19.0,
                'type_tax_use': 'sale',
                'tax_group_id': tax_group.id,
                'amount_type': 'percent',
            })

        return tax

    def update_product_details(self, values):
        if not isinstance(values, dict):
            raise ValidationError("Value is incorrect")
        self.write(values)
        print(f"I am updating this product{self.name}")
        return



class Joby(models.Model):
    _name = 'joby.joby'
    _description = 'joby.joby'

    name = fields.Char(string='Name')
    sale_description = fields.Char(string='Sale Description')
    sale_price = fields.Float(string='Sale Price')
    tex = fields.Char(string='Tex')
