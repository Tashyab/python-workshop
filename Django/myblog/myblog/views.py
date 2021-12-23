from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    return render(request, 'home.html')

def posts(request):
    return HttpResponse("Posts")

def about(request):
    return HttpResponse("About")

def contactus(request):
    return HttpResponse("contactus")

def signup(request):
    now=datetime.datetime.now()
    dt=now.strftime("%Y-%m-%d")
    dtdc={"today":dt}
    return render(request, 'signup.html', dtdc)

def policy(request):
    return render(request, 'policy.html')

def terms(request):
    return render(request, 'terms.html')