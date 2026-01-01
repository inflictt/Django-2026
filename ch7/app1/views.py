from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(req):
    return HttpResponse("<h1>Welcome</h1><br><i>User to the homepage !!!</i>")


def myapp1(req):
    return HttpResponse("<h1>Welcome</h1><br><i>User to the myapp1 page !!!</i>")
