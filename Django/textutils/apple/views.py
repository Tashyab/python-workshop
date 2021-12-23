#My file
from django.http import HttpResponse
from django.shortcuts import render
import string
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def analyzer(request):
    antext=request.GET.get("text",'default')
    rempunc=request.GET.get("rempunc", 'off')  
    upcase=request.GET.get("upcase", 'off')
    lowcase=request.GET.get("lowcase", 'off')
    exsprem=request.GET.get("exsprem", 'off')
    puncs=string.punctuation
    if rempunc=='on':
        ftext=" "
        for ch in antext:
            if ch not in puncs:
                ftext=ftext+ch
        antext=ftext

    if upcase=='on':
        antext=antext.upper()

    if lowcase=='on':
        antext=antext.lower()

    if exsprem=='on':
        antext=antext+" "
        ftext=" "
        for index, ch in enumerate(antext):
            if index+1<len(antext):
                if not (antext[index]==" " and antext[index+1]==" "):
                    ftext=ftext+ch
        antext=ftext

    if rempunc=='off' and upcase=='off' and lowcase=='off' and exsprem=='off':
        return HttpResponse("<h1>ERROR: Please check at least one box</h1> <br> <a href='/'>back</a>")

    para = {'purpose': "Analyzing conditions", 'analyzed': antext}
    return render(request, 'analyze.html', para)