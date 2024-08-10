from odoo import api,models,fields

class tag(models.Model):
    _name = 'tag'
    name = fields.Char(string= 'Bàn')
    time = fields.Datetime(string = 'Giờ')
    type_room = fields.Selection(string = 'Phòng' , selection= [('normal' , 'Thường') , ('vip' , 'V.I.P') , ('master' , 'Họp')])
    state = fields.Selection(string = 'Trạng thái' , selection= [('none' , 'Chưa Thanh Toán') , ('giai ngan' , 'Đã Thanh toán') ] , default = 'none')
    #note
    order_id = fields.One2many('order' , 'tag_id' , string= 'Order')
    price = fields.Integer(string= "Thành Tiền" , compute = 'get_price' , store=True)
    
    #button
    def action_order(self):
        self.state = 'none'
    def action_pay(self):
        self.state = 'giai ngan'
        for record in self.order_id:
            record.unlink()
    def action_latter(self):
        pass
    @api.depends('order_id.sum_price' , 'state')
    def get_price(self):
        for tag in self:
            if tag.state == 'giai ngan':
                for order in tag.order_id:
                    order.sum_price = 0                
            s = sum(order.sum_price for order in tag.order_id)
            tag.price = s