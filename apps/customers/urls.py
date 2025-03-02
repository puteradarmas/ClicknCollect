from django.urls import path
from django.contrib.auth import views as auth_views
from .views import user_logout,customer_register

urlpatterns = [
    path('register/', customer_register, name='customer_register'),
    path('login/', auth_views.LoginView.as_view(template_name='customers/login.html'), name='customer_login'),
    path('logout/', user_logout, name='logout'),
]