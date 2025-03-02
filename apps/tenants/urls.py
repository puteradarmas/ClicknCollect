from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home,tenant_register,tenant_logout

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='tenants/login.html'), name='tenant_login'),
    path('logout/', tenant_logout, name='logout'),
    path('register/', tenant_register, name='tenant_register'),
]
