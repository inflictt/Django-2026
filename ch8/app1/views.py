from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def learn_django(res, **kwargs):
    status = kwargs.get('status')
    print(status)
    return HttpResponse(f"<h1>Welcome usuer with status = {status} here and learn<br> <b>Django</b></h1>")
