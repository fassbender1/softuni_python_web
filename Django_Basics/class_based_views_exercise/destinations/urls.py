from django.urls import path

from destinations import views

app_name = 'destinations'
urlpatterns = [
    path('create/', views.DestinationCreateView.as_view(), name='create'),
    path('<int:pk>/', views.DestinationDetailView.as_view(), name='detail'),

]