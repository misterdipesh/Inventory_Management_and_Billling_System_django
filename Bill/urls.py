from django.urls import path
from .views import BillEdit,BillDelete,BillDetails,NewBill

urlpatterns = [
    path('register/', NewBill, name='add_bill'),
    path('details/', BillDetails, name='bill_details'),
    path('edit/<slug:slug>/', BillEdit, name='edit_bill'),
    path('delete/<slug:slug>/', BillDelete, name='delete_bill'),
]