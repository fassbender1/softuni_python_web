from django.urls import path, include

from posts import views

urlpatterns = [

    path('',views.IndexView.as_view(),name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add-post/', views.add_post, name='add-post'),
    path('<int:pk>/edit-post/', views.edit_post, name='edit-post'),
    path('<int:pk>/delete-post/', views.delete_post, name='delete-post'),
    path('<int:pk>/details-post/', views.details_post, name='details-post'),
]