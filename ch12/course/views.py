from django.shortcuts import render
from datetime import datetime
# Create your views here.

# eg1.0


# def dj(req):
#     return render(req, 'course/django.html', context={"cname": "inflict"})

# eg1.1- variables


def about(req):
    name = 'Django'
    duration = 'months'
    seats = '10'
    course_details = {"nm": name, "dur": duration, "seats": seats}
    return render(req, 'course/details.html', course_details)

# eg1.2- filkter


def filter(req):
    return render(req, 'course/filter.html', context={"cname": "filter", "description": "Hellow this is the best course on django ever kindly complete it on time ... "})


def datetime1(req):
    d = datetime.now()
    return render(req, 'course/datetime1.html', context={"dt": d})


def float(req):
    return render(req, 'course/django.html', context={"nm": "False"})


def floatt(req):
    stu = {"names": ['Rahul', 'Saksahm', 'Raj', 'Annu']}
    return render(req, 'course/django.html', context=stu)
