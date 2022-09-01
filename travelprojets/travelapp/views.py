from django.http import HttpResponse
from django.shortcuts import render
from .models import Team, Photoc

# Create your views here.
# def demo(request):
#     return HttpResponse("hello world")

# def demo(request):
#     # name="india"
#     return render(request,"home.html",{'obj':name})

def index(request):
    obj = Team.objects.all()
    obj1 = Photoc.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

# def about(request):
#     return render(request,"abouta.html")

def contact(request):
    return HttpResponse("Hello it's me contact")

def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res=x+y
    return render(request,'add.html',{'result1':res})