from django.forms import ModelForm
from .models import  Bill
class BillForm(ModelForm):
    class Meta:
        model=Bill
        fields='__all__'