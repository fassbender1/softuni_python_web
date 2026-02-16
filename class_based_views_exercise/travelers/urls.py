from travelers import views
from django.urls import path

app_name = 'travelers'

urlpatterns = [
    path('create/', views.TravelerCreateView.as_view(), name='create'),

]