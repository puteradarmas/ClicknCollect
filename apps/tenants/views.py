from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import TenantRegisterForm


@login_required
def home(request):
    return render(request, 'tenants/home.html')


def tenant_register(request):
    if request.method == "POST":
        form = TenantRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = TenantRegisterForm()
    return render(request, "tenants/tenants_register.html", {"form": form})

@login_required
def ongoing_order(request):
    return render(request, "tenants/ongoing_order.html")

@login_required
def inventory(request):
    return render(request, "tenants/inventory.html")

@login_required
def order_status(request):
    return render(request, "tenants/order_status.html")

@login_required
def picking_up(request):
    return render(request, "tenants/picking_up.html")


def tenant_logout(request):
    logout(request)
    return redirect("tenant_login")