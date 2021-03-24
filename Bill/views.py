from django.shortcuts import render,redirect,HttpResponse
from .forms import BillForm
from .models import Bill,SoldItem
from Product.models import Product
from Customer.models import Customer
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
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

                 'date':datetime.now,
                 }
        return render(request, "invoice_print.html", context)
    else:
        return render(request,'select_customer.html')
@login_required(login_url='/login/')
def SalesDetails(request):
    sales=SoldItem.objects.all()
    context={'sales':sales}
    template='sales_details.html'
    return render(request,template,context)
def UserLogin(request):
    if request.user.is_authenticated:
        return redirect('scanner')
    else:
        context={}
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)

                return redirect('scanner')
            else:
                context={'error':"Invalid User or Password"}
        return render(request,'login.html',context)
def LogoutUser(request):
    logout(request)
    return redirect('login')