from django.urls import path

from department.views import index

urlpatterns = [
    path('department/<id>/', index),
    path('department/<int:id>/', index),

]