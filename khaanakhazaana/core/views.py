from django.shortcuts import render

# Create your views here.


def home(req):
    return render(req,'core/home.html')

def base(req):
    return render(req,'core/base.html')
def about(req):
    return render(req,'core/about.html')
def contact(request):
    return render(request, 'core/contact.html')
