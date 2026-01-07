from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactForm

def contact_form(request):
    return render(request, 'ch22/contact_form.html')

def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        if name and message:
            ContactForm.objects.create(name=name, message=message)
            return HttpResponse(
                f"Thank you {name}, your message '{message}' was received!"
            )
        else:
            return HttpResponse(
                "Please fill all fields correctly.",
                status=400
            )

    return redirect('contact_form')
