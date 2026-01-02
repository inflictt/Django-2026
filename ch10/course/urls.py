from django.urls import path
from course.views import learn_django

urlpatterns = [
    path("learn_django/", learn_django)
]
