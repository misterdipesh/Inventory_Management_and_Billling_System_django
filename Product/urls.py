from django.urls import path
from .views import RegisterProduct,ShowProduct,EditProduct,DeleteProduct

urlpatterns = [
    path('register/',RegisterProduct,name='register_product'),
    path('',ShowProduct,name='details_product'),
    path('edit/<slug:slug>/',EditProduct,name='edit_product'),
    path('delete/<slug:slug>/',DeleteProduct,name='delete_product')

]