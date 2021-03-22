from django.db import models
from Customer.models import Customer
from Product.models import  Product
from django.template.defaultfilters import slugify
class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Bought By',null=True)
    bill_amount=models.IntegerField(verbose_name='Amount')
    bill_date=models.DateTimeField(auto_now_add=True,verbose_name='Date',null=True)
    def __str__(self):
        return str(self.id)


class SoldItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='Product')
    quantity = models.IntegerField(verbose_name='Quantity')
    individual_price=models.FloatField(verbose_name='Amount')
    bill_no=models.ForeignKey(Bill,on_delete=models.CASCADE,verbose_name='Bill NO.')
