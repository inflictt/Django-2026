from django.urls import path
from . import views         
app_name = "accounts"   
urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),      
    path("dashboard/", views.dashboard_view, name="dashboard"),

    path("change-password/", views.change_password, name="change_password"),
    path("reset-password/", views.reset_password, name="reset_password"),
    path("reset-password-confirm/<uidb64>/<token>/", views.reset_password_confirm, name="reset_password_confirm"),
]