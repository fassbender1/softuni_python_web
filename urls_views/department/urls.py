from django.urls import path

from department.views import index

urlpatterns = [
    path('', index),
]