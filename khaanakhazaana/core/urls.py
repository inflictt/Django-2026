from django.urls import path
from core.views import home, base,about,contact

urlpatterns = [
    path('home/',home,name='home'),
    path('base/',base,name='base'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
]
