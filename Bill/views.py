from django.shortcuts import render,redirect,HttpResponse
from .forms import BillForm
from .models import Bill,SoldItem
from Product.models import Product
from Customer.models import Customer
def SellingItems(request):
    bill = Bill.objects.create(bill_amount=0)
    context = {'message': '',
               'bill': bill}

    if request.method=="POST":
        barcode=int(request.POST.get('barcode'))
        quantity = int(request.POST.get('quantity'))

        product=Product.objects.get(product_barcode=barcode)
        product.product_quantity-=quantity
        product.save()
        amount=float(product.product_price*quantity)
        items=SoldItem.objects.create(product=product,quantity=quantity,bill_no=bill,individual_price=amount)

        items.save()


        return render(request,'barcodeaddproduct.html',{'message': 'added','bill':bill})

    else:
        return render(request,'barcodeaddproduct.html',context)

def Invoice(request,id):
    if request.method=='POST':
        customer_email=request.POST.get('customer')
        customer=Customer.objects.get(customer_email=customer_email)
        bill=Bill.objects.get(id=id)
        bill.customer=customer
        print(bill.customer)
        amount=0
        product=SoldItem.objects.all().filter(bill_no=bill.id)


        for item in product:
            product_item=Product.objects.get(id=item.product.id)
            amount=product_item.product_price*item.quantity
        bill.bill_amount=amount
        bill.save()
        context={'amount':amount,
                 'customer':customer,
                 'items':product,
                 'bill':bill.id,
                 }
        return render(request, "invoice_print.html", context)
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
