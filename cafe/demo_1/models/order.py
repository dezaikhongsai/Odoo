from odoo import api,models,fields

class order(models.Model):
    _name = 'order'
    tag_id = fields.Many2one('tag' , string= 'Thẻ bàn')
    menu_id = fields.Many2many('menu' , string = 'Đồ Uống')
    qty = fields.Integer(string= 'Số lượng')
    price_unit = fields.Float(string = 'Giá mỗi đồ uống' , compute = 'get_price_unit' , store=True)
    sum_price = fields.Float(string = 'Thành tiền' , compute = 'get_sum_price' ,store=True)
    @api.depends('menu_id')
    def get_price_unit(self):
        for order in self:
            if order.menu_id:
                order.price_unit = sum(menu.price for menu in order.menu_id) 
            else:
                order.price_unit = 0.0
    
    @api.depends('qty' , 'price_unit')
    def get_sum_price(self):
        for order in self:
            order.sum_price = order.qty * order.price_unit    
            