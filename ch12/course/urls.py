from django.urls import path
from course.views import about as about
from course.views import filter as filter
from course.views import datetime1 as datetime1
from course.views import floatt as floatt
urlpatterns = [
    path('about/', about),
    path('filter/', filter),
    path('datetime1/', datetime1),
    path('floatt/', floatt),
]
