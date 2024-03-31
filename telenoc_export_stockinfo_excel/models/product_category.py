# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductCategory(models.Model):
    """Inherit the 'product_category' to add the 'stock_report_ids' field,
    which should be set as invisible."""
    _inherit = 'product.category'

    stock_report_ids = fields.Many2many('stock.xls.report',
                                        string="Stock Report",
                                        help="Retrieve Stock Report IDs.",
                                        invisible=True)
