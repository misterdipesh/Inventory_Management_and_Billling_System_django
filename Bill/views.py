from django.shortcuts import render,redirect,HttpResponse
from .forms import BillForm
from .models import Bill,TemporatyStorage,SoldItem
from Product.models import Product
from Customer.models import Customer
def SellingItems(request):
    if request.method=="POST":
        barcode=int(request.POST.get('barcode'))
        quantity = int(request.POST.get('quantity'))
        try:
            product=Product.objects.get(product_barcode=barcode)
            print(product)
            items=TemporatyStorage.objects.create(items=product,quantity=quantity)
            items.save()
            return render(request,'barcodeaddproduct.html',{'message':'Item added'})
        except:
            return HttpResponse("NOT FOUND")
    else:
        return render(request,'barcodeaddproduct.html',{'message':''})

def Invoice(request):
    if request.method=='POST':
        customer_email=request.POST.get('customer')
        customer=Customer.objects.get(customer_email=customer_email)
        items=TemporatyStorage.objects.all()
        amount=0
        for item in items:
            product=Product.objects.get(id=item.items.id)
            amount+=item.quantity*product.product_price
            print(amount)
        bill=Bill.objects.create(bill_amount=amount)
        bill.save()
        for item in items:
            product = Product.objects.get(id=item.items.id)
            sellitem=SoldItem.objects.create(customer=customer,product=product,bill_quantity=item.quantity,bill_no=bill)
            sellitem.save()

        context={'amount':amount,
                 'items':items,
                 'customer':customer,
                 'bill':bill.id
                 }
        items.delete()
        return render(request,"invoice_print.html",context)
    else:
        return render(request,'select_customer.html')

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
    bills=Bill.objects.all()
    context={'bills':bills}
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
