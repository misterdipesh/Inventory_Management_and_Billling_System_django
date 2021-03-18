from django.db import models
class Customer(models.Model):
    customer_name=models.CharField(max_length=100,verbose_name='Customer Full Name')
    customer_address=models.CharField(max_length=100,verbose_name='Address')
    customer_number=models.CharField(max_length=20,verbose_name='Phone Number')
    def __str__(self):
        return self.customer_name

