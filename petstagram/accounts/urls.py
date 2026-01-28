from django.urls import path, include

from accounts import views

app_name = 'accounts'

profile_patterns = [
        path('', views.profile_details, name='profile_details'),
        path('edit/', views.profile_edit, name='profile_edit'),
        path('delete/', views.profile_delete, name='profile_delete'),
]

authentication_patterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]

urlpatterns = [
    path('', include(authentication_patterns)),
    path('profile/<int:pk>', include(profile_patterns))
]