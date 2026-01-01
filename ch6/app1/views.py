from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # logicis written here
    return HttpResponse("Hellow django to you homePage.!!1")


def myfunction(request):
    # logicis written here
    return HttpResponse("Hellow django")


def myfunction1(request):
    # logicis written here
    return HttpResponse("Hellow inflict")
