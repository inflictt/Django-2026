from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def ld_dj(req, **kwargs):
    status = kwargs.get('status')
    return HttpResponse(f"Here we welcom anothere user app2 with status as : {status}")
