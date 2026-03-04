from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('fbv/login/', views.login_fbv, name='login-fbv'),
    path('fbv/logout/', views.logout_fbv, name='logout-fbv'),
    path('fbv/register/', views.register_fbv, name='register-fbv'),
    path('cbv/login/', LoginView.as_view(template_name='accounts/login.html'), name='login-cbv'),
    path('cbv/logout/', LogoutView.as_view(), name='logout-cbv'),
    path('details/', views.ProfileView.as_view(), name='detail'),
]