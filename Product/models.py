from django.db import models
class Product(models.Model):
    product_name=models.CharField(max_length=100,verbose_name='Product Name')
    product_brand=models.CharField(max_length=100,verbose_name='Product Brand')
    product_quantity=models.IntegerField(verbose_name='Quantity')
    product_price=models.IntegerField(verbose_name='Price')
    product_mfd=models.DateField(verbose_name='Manufacturing Date')
    product_exp=models.DateField(verbose_name='Expiry Date')

    def __str__(self):
        return self.product_name
