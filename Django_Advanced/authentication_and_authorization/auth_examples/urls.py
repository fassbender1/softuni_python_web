from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from auth_examples import views
from auth_examples.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('fbv/login/', views.login_fbv, name='login-fbv'),
    path('fbv/logout/', views.logout_fbv, name='logout-fbv'),
    path('fbv/register/', views.register_fbv, name='register-fbv'),
    path('cbv/login/', LoginView.as_view(template_name='fbv/login.html'), name='login-cbv'),
    path('cbv/logout/', LogoutView.as_view(), name='logout-cbv'),
]