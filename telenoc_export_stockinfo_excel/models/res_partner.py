# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    """Inherit the 'res_partner' to add the 'stock_report_ids' field,
        which should be set as invisible."""
    _inherit = 'res.partner'

    stock_report_ids = fields.Many2many('stock.xls.report',
                                        string="Stock Report",
                                        help="Retrieve Stock Report IDs.",
                                        invisible=True)
