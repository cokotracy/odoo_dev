# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class LibraryBookCopy(models.Model):
    _name = "library.book.copy"
    _inherit = "library.book"
    _description = "Library Book's Copy"    