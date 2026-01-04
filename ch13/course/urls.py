from django.urls import path
from course.views import ld_dj as ld_dj
urlpatterns = [
    path('dj/', ld_dj),
]
