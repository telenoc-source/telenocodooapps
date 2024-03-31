# -*- coding: utf-8 -*-
from odoo import fields, models


class PosConfig(models.Model):
    """Inherited pos config for uploading logo image"""
    _inherit = 'pos.config'

    image = fields.Binary(string='Image', help="Set logo image for viewing it"
                                               "in POS Screen and Receipt")
