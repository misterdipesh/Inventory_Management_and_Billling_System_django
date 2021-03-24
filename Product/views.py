from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import  ProductForm
from .models import Product
@login_required(login_url='/login/')
def RegisterProduct(request):
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('details_product')
    form=ProductForm()
    context={'form':form}
    template='add_products.html'
    return render(request,template,context)
@login_required(login_url='/login/')
def ShowProduct(request):
    product=Product.objects.all()
    template='details_product.html'
    context={
        'products':product
    }
    return render(request,template,context)
@login_required(login_url='/login/')
def EditProduct(request,slug):
    product = Product.objects.get(slug=slug)
    if request.method=="POST":
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('details_product')
    form=ProductForm(instance=product)
    template='edit_products.html'
    context={
        'form':form
    }
    return render(request,template,context)
@login_required(login_url='/login/')
def DeleteProduct(slug):
    product=Product.objects.get(slug=slug)
    product.delete()
    return redirect('details_product')
