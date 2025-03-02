from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomerRegisterForm

@login_required
def home(request):
    return render(request, 'customers/home.html')

def customer_register(request):
    if request.method == "POST":
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomerRegisterForm()
    return render(request, "customers/customer_register.html", {"form": form})

def user_login(request):
    return render(request, "customers/login.html")

def user_logout(request):
    logout(request)
    return redirect("customer_login")