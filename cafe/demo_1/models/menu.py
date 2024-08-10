from odoo import api,models,fields

class  menu(models.Model):
    _name = 'menu'
    order_id = fields.Many2many('order' ,  string= 'ID')
    img =  fields.Binary(string='Ảnh')
    category = fields.Selection(string = 'Thể loại', selection=[('coffe' , 'Coffe') , ('tea' , 'Trà') , ('uncategory' , 'Đồ Uống Khác')])
    product = fields.Char(string = 'Sản phẩm')
    price = fields.Integer(string = 'Giá')