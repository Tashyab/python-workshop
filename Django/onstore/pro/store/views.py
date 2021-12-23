from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    allprods=[]
    catprods=Product.objects.values('category', 'id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslides= n//4 + 1
        if n%4==0:
            nslides=n//4
        allprods.append([prod, range(1, nslides), nslides])
    
    params={'allprods': allprods}
    return render (request, 'store/index.html', params)

def about(request):
    return render (request, 'store/about.html')

def search(request):
    return HttpResponse("Searching Store")

def contact(request):
    return HttpResponse("Contact Store")

def tracker(request):
    return HttpResponse("Tracking status")

def proview(request):
    return HttpResponse("Viewing product")

def checkout(request):
    return HttpResponse("You are checking out")