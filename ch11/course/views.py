from django.shortcuts import render

# Create your views here.


def ld_dj(req):

    coursename = {"cname": "inflict"}

    return render(req, 'course/django.html', context=coursename)
