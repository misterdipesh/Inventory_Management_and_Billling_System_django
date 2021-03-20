from django.db import models
from django.template.defaultfilters import slugify
class Customer(models.Model):
    customer_name=models.CharField(max_length=100,verbose_name='Customer Full Name')
    customer_address=models.CharField(max_length=100,verbose_name='Address')
    customer_number=models.CharField(max_length=20,verbose_name='Phone Number',unique=True)
    customer_email=models.EmailField(unique=True,null=True,default="xyz@abc.com")
    slug=models.SlugField(null=True,unique=True,blank=True)
    def __str__(self):
        return self.customer_email

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.customer_number)
        return super().save(*args, **kwargs)

