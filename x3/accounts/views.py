from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            login(request,user=form.get_user())

            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}. You can now log in.")
            return render(request, "accounts/login.html")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "accounts/dashboard.html")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return render(request, "accounts/login.html")   

@login_required
def dashboard_view(request):
    return render(request, "accounts/dashboard.html")       
@login_required
def change_password(request):
    pass    
@login_required
def reset_password(request):
    pass
def reset_password_confirm(request, uidb64, token):
    pass
