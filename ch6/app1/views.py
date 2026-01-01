from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def myfunction(request):
    # logicis written here
    return HttpResponse("Hellow django")


def myfunction1(request):
    # logicis written here
    return HttpResponse("Hellow inflict")
