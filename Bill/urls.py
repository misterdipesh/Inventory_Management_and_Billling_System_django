from django.urls import path
from .views import BillEdit,BillDelete,BillDetails,NewBill,SellingItems,Invoice,SalesDetails

urlpatterns = [
    path('register/', NewBill, name='add_bill'),
    path('details/', BillDetails, name='bill_details'),
    path('edit/<slug:slug>/', BillEdit, name='edit_bill'),
    path('delete/<slug:slug>/', BillDelete, name='delete_bill'),
    path('scan/',SellingItems,name='scanner'),
    path('billprint/<int:id>/',Invoice,name='print_bill'),
    path('salesdetails',SalesDetails,name='sales_details')
]