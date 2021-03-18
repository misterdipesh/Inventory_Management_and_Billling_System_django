from django.db import models
from Customer.models import Customer
from Product.models import  Product
class Bill(models.Model):
    bill_customer=models.ForeignKey(Customer,on_delete=models.CASCADE,verbose_name='Bought By')
    bill_amount=models.IntegerField(verbose_name='Amount')
    bill_date=models.DateTimeField(auto_now_add=True,verbose_name='Date')
    bill_product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='Product')
    bil_quantity=models.IntegerField(verbose_name='Quantity')
