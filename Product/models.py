from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
class Product(models.Model):
    product_name=models.CharField(max_length=100,verbose_name='Product Name')
    product_brand=models.CharField(max_length=100,verbose_name='Product Brand')
    product_quantity=models.IntegerField(verbose_name='Quantity', validators=[MinValueValidator(0)])
    product_price=models.FloatField(verbose_name='Price')
    product_mfd=models.DateField(verbose_name='Manufacturing Date')
    product_exp=models.DateField(verbose_name='Expiry Date')
    product_barcode=models.IntegerField(verbose_name="Barcode Number",unique=True,null=True)
    slug=models.SlugField(null=True,unique=True,blank=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.product_name)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.product_name
