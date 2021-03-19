from django.shortcuts import render,redirect
from .forms import CustomerRegistrationForm
from .models import Customer
def CustomerRegister(request):
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_customer')
    form=CustomerRegistrationForm
    context={'form':form}
    template='customer_register.html'
    return render(request,template,context)
def CustomerDetails(request):
    customer=Customer.objects.all()
    template='details_customer.html'
    context={'customer':customer}
    return render(request,template,context)
def CustomerEdit(request,slug):
    customer = Customer.objects.get(slug=slug)
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details_customer')
    form=CustomerRegistrationForm(instance=customer)
    context={'form':form}
    template='customer_edit.html'
    return render(request,template,context)
def CustomerDelete(slug):
    customer=Customer.objects.get(slug=slug)
    customer.delete()
    return redirect('details_customer')



