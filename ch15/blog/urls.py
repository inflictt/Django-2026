from django.urls import path

from blog.views import first 

urlpatterns = [
    path('first/',first)
]
