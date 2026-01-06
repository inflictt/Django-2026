from django.shortcuts import render

# Create your views here.
def first(req):
    return render(req,'ch15/first.html')