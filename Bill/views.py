from django.shortcuts import render,redirect
from .forms import BillForm
from .models import Bill
def NewBill(request):
    if request.method=="POST":
        form=BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_details')
    form=BillForm()
    template='bill_add.html'
    context={'form':form}
    return render(request,template,context)
def BillDetails(request):
    bill=Bill.objects.all()
    context={'bill':bill}
    template='bill_details.html'
    return render(request,template,context)
def BillEdit(request,slug):
    bill = Bill.objects.get(slug=slug)
    if request.method=="POST":
        form=BillForm(request.POST,instance=bill)
        if form.is_valid():
            form.save()
            return redirect('bill_details')
    form=BillForm(instance=bill)
    context={'form':form}
    template='bill_edit.html'
    return render(request,template,context)
def BillDelete(slug):
    bill=Bill.objects.get(slug=slug)
    bill.delete()
    redirect('bill_details')
