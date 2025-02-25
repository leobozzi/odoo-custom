# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
import time
from odoo.tools.translate import _
import odoo.addons.decimal_precision as dp
from datetime import datetime, timedelta, date

class GiftVoucher(models.Model):
    _name = "gift.voucher"
    
    name = fields.Char('Code')
    comment = fields.Text('Comment')
    amount = fields.Float('Amount')
    used = fields.Boolean('Used')


class product_product(models.Model):
    _inherit = 'product.template'
    
    denomination =  fields.Boolean('Denomination')

class sale_order(models.Model):
    _inherit = 'sale.order'
    
    gift_voucher_id = fields.Many2one('gift.voucher', 'Gift Voucher')
    
    
    def write(self ,vals):
        if vals.get('message'):
            if self.order_line:
                for line in self.order_line:
                    product = self.env['product.product'].search([('id','=',line.product_id.id)])[0]
                    if product.denomination  == True:
                        voucher_obj = self.env['gift.voucher']
                        search_voucher = voucher_obj.search([('used','=', False)])
                        if search_voucher:
                            values = { 'used' : True,
                                      'comment' : vals.get('message'),
                                      'amount' : line.product_uom_qty,
                            }
                            write_voucher = search_voucher[0].write(values)
                            vals.update({'gift_voucher_id': search_voucher[0].id})
        res= super(sale_order , self).write(vals)
        return res