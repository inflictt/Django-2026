from django.urls import path

from course.views import ld_dj

urlpatterns = [
    path('ld_dj', ld_dj)
]
