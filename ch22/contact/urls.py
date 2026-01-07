from django.urls import path
from .views import contact_form, submit

urlpatterns = [
    path('contact_form/', contact_form, name='contact_form'),
    path('submit/', submit, name='submit'),
]
