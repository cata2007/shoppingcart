from django.shortcuts import render
from .models import Category,Product


def product_list(request):
 categories = Category.objects.all()
 products = Product.objects.all()

 context={
    'products':products,
    'categories':categories
 }
 return render(request,'list.html',context)
# Create your views here.
