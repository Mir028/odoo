# -*- coding: utf-8 -*-
from multiprocessing.reduction import duplicate

from odoo import fields, models, api
import time

from odoo.addons.test_convert.tests.test_env import record
from odoo.exceptions import UserError


class InheritedSaleOrder(models.Model):
    _inherit = 'product.template'
    description_sale = fields.Text(string='SAle Description')


class School(models.Model):
    _name = 'school.school'

    image = fields.Image(string='School Image')
    name = fields.Char(string='Name')
    student_list = fields.One2many('student.student', 'school_id', string='Students')
    number = fields.Integer(string='Number')
    invoice_id = fields.Many2one('account.move', string='Invoice')
    invoice_user_id = fields.Many2one('res.users', string='Invoice User', related='invoice_id.invoice_user_id')
    invoice_date = fields.Date(string='Invoice Date', related='invoice_id.invoice_date')
    location = fields.Char(string='Location')
    ref_field_id = fields.Reference([('school.school',''), ('student.student',''), ('sale.order',''), ('account.move','')], string='Reference Field')
    binary_field = fields.Binary(string='Binary')
    binary_fields = fields.Many2many("ir.attachment", string='Multy Attachments')
    currency_id = fields.Many2one('res.currency', string='Currency')
    amount = fields.Monetary(string='Amount')

    #@api.model
    @api.model_create_multi
    #@api.model_create_single
    def create(self, vals):
        rtn = super(School, self).create(vals)
        return rtn
        # self.name = "Single Update"
        # self.amount = 40
        # self.update({'name':'Write Update', "amount":40})

        # self.write({'name':'Write Update', "amount":40})



    def write(self, vals):
        print("Write method")
        print(self)
        print(vals)
        rtn = super(School, self).write(vals)
        return rtn


class Student(models.Model):
    _name = "student.student"
    _description = "Student"

    def duplicate_record(self):
        print(self)
        duplicate_record = self.copy()
        print(duplicate_record)

    @api.returns("self",lambda value: value.id)
    def copy(self,default=None):
        print(self)
        print(default)
        rtn = super(Student, self).copy(default)
        print(rtn)

    name = fields.Char(string="Name")
    name1 = fields.Char(string="Name1")
    name2 = fields.Char(string="Name2")
    name3 = fields.Char(string="Name3")
    name4 = fields.Char(string="Name4")

    school_id = fields.Many2one('school.school', string="Student")

    student_name = fields.Char(string="Student Name",required=True)
    address_html = fields.Html(string="Address HTML")
    gender = fields.Selection([('female', 'Female'), ('male', 'Male')], string="Gender")
    number = fields.Integer(string="Number")
    student_fees = fields.Float(string="Student Fees")
    school_data = fields.Json(string="School Data")
    joining_date = fields.Date(string="Joining Date",default=fields.Date.today)
    start_date = fields.Date(string="Start Date",default=time.strftime("%Y-%m-%d"))
    end_date = fields.Date(string="End Date",default=time.strftime("%Y-%m-%d"))
    date_time = fields.Datetime(string="Date",defualt=fields.Datetime.today)
    discount = fields.Float(string="Discount")
    final_fees = fields.Float(string="Final Fees",compute='_compute_final_fees_value')
    compute_address_html = fields.Html(string="Address HTML")

    @api.onchange('address_html')
    def onchange_address_html_field(self):
        for record in self:
            record.compute_address_html = record.address_html

    def _compute_final_fees_value(self):
        for record in self:
            record.final_fees += record.student_fees - record.discount

    def json_data_store(self):
        self.school_data = {"name":self.name, "fees":self.student_fees, "number":self.number}

    def custom_method(self):
        print(self.read(fields=['name']))
        student_group = self.env["school.school"].read_group([],["name"], ['name'])
        for i in student_group:
            print(i)

        # record = self.env['school.school'].search([('name', '=', 'Miro')])
        # print(record)

        # total_records = self.env['school.school'].search_count([('id','>',1)], limit=10)
        # print(total_records)

        # data = {"name":"WebLearns-1-Record"}
        # self.env["school.school"].create(data)

        # records = self.env['school.school'].search([('name', '!=', 'Miro')])
        # print("Records with name != 'Miro':", records)

        # records = self.env['school.school'].search([('name', 'ilike', 'Academy')])
        # print(records)

        # records = self.env['school.school'].search([('name', '=like', 'M%')])
        # print(records)

        # records = self.env['school.school'].search([('id', 'in', [2, 3, 5])])
        # print(records)

        # records = self.env['school.school'].search([('id', 'not in', [2, 3, 5])])
        # print(records)


        # records = self.env['school.school'].search([('create_date', '>', '2024-01-01')])
        # print(records)

        # records = self.env['school.school'].search([('is_active', '=', True)])
        # print(records)

        # records = self.env['school.school'].search([
        #     ('name', 'ilike', 'Academy'),
        #     ('id', '>', 1)
        # ])
        # print(records)

        # records = self.env['school.school'].search([
        #     '|',  # OR operator
        #     ('name', 'ilike', 'Academy'),
        #     ('id', '<', 5)
        # ])
        # print(records)

        # records = self.env['school.school'].search([
        #     '|',
        #     ('name', 'ilike', 'Academy'),
        #     ('id', '<', 5),
        #     ('is_active', '=', True)
        # ])
        # print(records)

        # records = self.env['school.school'].search([
        #     ('name', 'not ilike', 'Academy'),
        #     ('id', '>', 10)
        # ])
        # print(records)

        # records = self.env['school.school'].search([
        #     '|',
        #     ('parent_id.name', '=', 'Main School'),
        #     ('parent_id.name', '=', 'Secondary School'),
        #     ('id', '>', 2)
        # ])
        # print("Records with specific parent name AND ID > 2:", records)


        # records = self.env['school.school'].search([('parent_id.name', '=', 'Main School')])
        # print(records)

        # records = self.env['school.school'].search([('description', '=', False)])
        # print(records)

        # limited_records = self.env['school.school'].search([('id', '>', 1)], limit=10)
        # print(limited_records)

        # total_records = self.env['school.school'].search_count([('name', 'ilike', 'Academy')])
        # print(total_records)

        # total_records = self.env['school.school'].search_count([('is_active', '=', True)])
        # print(total_records)

        # total_records = self.env['school.school'].search_count([('description', '=', False)])
        # print(total_records)


    def delete_record(self):
        print(self)
        shcool_id = self.env["school.school"].browse(12)
        for school in shcool_id:
            if not school.exists():
                raise UserError(f"Record is not available {school}")
            else:
                print("Instance or Record exists", school)
        print(shcool_id)
        print(shcool_id.unlink())

    def unlink(self):
        rtn = super(Student, self).unlink()
        return rtn


