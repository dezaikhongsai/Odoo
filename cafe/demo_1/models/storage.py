from odoo import api,models,fields

class  storage(models.Model):
    _name = 'storage'
    img =  fields.Binary(string='Ảnh')
    category = fields.Selection(string = 'Thể loại', selection=[('nguyen lieu pha che' , 'Nguyên liệu pha chế') , ('vật liệu stepup' , 'Vật liệu stepup') , ('uncategory' , 'Uncategory')])
    product = fields.Char(string = 'Sản phẩm')
    date = fields.Datetime(string = 'Ngày nhập hàng')
    inventory_num = fields.Integer(string = 'Số lượng nhập')
    amount = fields.Integer(string = 'Số Lượng tồn kho')
    price = fields.Integer(string = "Đơn Giá")
    lastofprice = fields.Integer(string = "Thành tiền theo tháng" , compute= 'get_sum' , store=True)
    
    def action_taken(self):
        self.inventory_num  += 1
        self.amount += 1
    def action_consum(self):
        self.amount -=1
    def action_reset(self):
        self.inventory_num = 0
        self.amount = 0
    @api.depends('inventory_num' , 'price' , 'lastofprice')
    def get_sum(self):
        for storage in self:
            storage.lastofprice =  storage.inventory_num * storage.price
   