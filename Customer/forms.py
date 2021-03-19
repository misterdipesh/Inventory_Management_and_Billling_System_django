from django.forms import ModelForm
from .models import Customer
class CustomerRegistrationForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
