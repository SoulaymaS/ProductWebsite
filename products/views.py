from django.shortcuts import render

# Create your views here.
from .models import Product, Supplier

def indexP(request):
    result=Product.objects.all()
    context={"listProducts":result}
    return render(request, 'products/product.html',context)

def indexS(request):
    result=Supplier.objects.all()
    context={"listSupplier":result}
    return render(request, 'products/product.html',context)

def getProduct(request,product_id):
    result=Product.objects.get(pk=product_id)
    context={"listProducts":result}
    return render(request, 'products/details.html',context)

def getSupplier(request,product_id):
    result=Product.objects.get(pk=product_id)
    context={"listProducts":result}
    return render(request, 'products/details.html',context)
def details(request):
    return render(request,"products/details.html")