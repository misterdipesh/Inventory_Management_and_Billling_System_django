from django.shortcuts import render,redirect
from .forms import CustomerRegistrationForm
from .models import Customer
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
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
@login_required(login_url='/login/')
def CustomerDetails(request):
    customers=Customer.objects.all()
    template='details_customer.html'
    context={'customers':customers}
    return render(request,template,context)
@login_required(login_url='/login/')
def CustomerEdit(request,slug):
    customer = Customer.objects.get(slug=slug)
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('details_customer')
    form=CustomerRegistrationForm(instance=customer)
    context={'form':form}
    template='customer_edit.html'
    return render(request,template,context)
@login_required(login_url='/login/')
def CustomerDelete(slug):
    customer=Customer.objects.get(slug=slug)
    customer.delete()
    return redirect('details_customer')



