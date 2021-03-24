from django.urls import path
from .views import SellingItems,Invoice,SalesDetails,UserLogin

urlpatterns = [
    path('',SellingItems,name='scanner'),
    path('billprint/<int:id>/',Invoice,name='print_bill'),
    path('salesdetails',SalesDetails,name='sales_details'),
    path('login',UserLogin,name='login')
]