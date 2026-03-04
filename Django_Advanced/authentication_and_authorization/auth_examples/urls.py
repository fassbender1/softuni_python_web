from django.urls import path

from auth_examples import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fbv/login/', views.login_fbv, name='login-fbv'),
    path('fbv/logout/', views.logout_fbv, name='logout-fbv'),
    path('fbv/register/', views.register_fbv, name='register-fbv'),
]