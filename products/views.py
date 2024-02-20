from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Offer

# Create your views here.

def index(request):
    #return HttpResponse("Products Page")

    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products':products})

def newprod(request):
    return HttpResponse('New Products')
