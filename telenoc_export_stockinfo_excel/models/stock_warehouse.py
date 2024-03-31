# -*- coding: utf-8 -*-
from odoo import fields, models


class StockWarehouse(models.Model):
    """Inherit the 'stock_warehouse' to add the 'stock_report_ids' field,
        which should be set as invisible."""
    _inherit = 'stock.warehouse'

    stock_report_ids = fields.Many2many('stock.xls.report',
                                        string="Stock Report",
                                        help="Retrieve Stock Report IDs.",
                                        invisible=True)
