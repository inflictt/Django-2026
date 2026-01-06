from django.urls import path

from portfolio.views import port,student_list

from portfolio.models import Student

urlpatterns = [
    path('port/',port,name='port'),
    path('stu_list/',student_list,name='stu_list'),
]
