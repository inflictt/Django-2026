from django.shortcuts import render
from portfolio.models import Student

# Create your views here.
def port(req):
    return render(req,'ch21/portfolio.html')

def student_list(req):
    students=Student.objects.all()
    return render(req,'ch21/student_list.html',{"students":students})