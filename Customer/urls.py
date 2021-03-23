
from django.urls import path
from .views import CustomerRegister,CustomerDetails,CustomerEdit,CustomerDelete


urlpatterns = [
    path('register/',CustomerRegister,name='register_customer'),
    path('',CustomerDetails,name='details_customer'),
    path('edit/<slug:slug>/',CustomerEdit,name='edit_customer'),
    path('delete/<slug:slug>/',CustomerDelete,name='delete_customer'),

]