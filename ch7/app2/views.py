from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def myapp2(req):
    return HttpResponse("<h3>Welcome</h3><br><b>User to the myapp2 page !!!</b>")
