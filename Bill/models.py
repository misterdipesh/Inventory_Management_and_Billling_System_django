from django.db import models
from Customer.models import Customer
from Product.models import  Product
from django.template.defaultfilters import slugify
class Bill(models.Model):
    bill_customer=models.ForeignKey(Customer,on_delete=models.CASCADE,verbose_name='Bought By')
    bill_amount=models.IntegerField(verbose_name='Amount')
    bill_date=models.DateTimeField(auto_now_add=True,verbose_name='Date')
    bill_product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='Product')
    bil_quantity=models.IntegerField(verbose_name='Quantity')
    slug=models.SlugField(null=True,unique=True)
    def __str__(self):
        return self.bill_customer

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = '-'.join(slugify(self.bill_customer), slugify(self.bill_date),slugify(self.bill_product))
        return super().save(*args, **kwargs)
