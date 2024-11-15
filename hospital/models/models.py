# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Hospital(models.Model):
    _name = 'hospital.hospital'
    _description = 'hospital.hospital'

    name = fields.Char()