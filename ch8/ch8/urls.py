
from django.contrib import admin
from django.urls import path
from app1 import views as app1
from app2 import views as app2

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app1/", app1.learn_django,
         {"status": "Kem Paalty"}, name='learn_django'),
    path("app2/", app2.ld_dj, {"status": " bhai bhai"}, name='ld_dj'),
]
