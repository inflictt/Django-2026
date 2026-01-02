from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def learn_django(req):
    # return render(req, template_name=learn_django, context=, content_type=, status=, using=)
    return render(req, 'course/django.html')
