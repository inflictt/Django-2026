from django.shortcuts import render

# Create your views here.


def ld_dj(req):
    name = {"name": "Lakshya"}
    return render(req, 'course/django.html', name)
