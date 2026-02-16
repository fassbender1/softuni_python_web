from django.urls import path, include

from posts import views

urlpatterns = [

    path('redirect/', views.MyRedirectView.as_view()),
    path('',views.IndexView.as_view(),name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add-post/', views.AddPostView.as_view(), name='add-post'),
    path('<int:pk>/edit-post/', views.EditPostView.as_view(), name='edit-post'),
    path('<int:pk>/delete-post/', views.DeletePostView.as_view(), name='delete-post'),
    path('<int:pk>/details-post/', views.DetailsPostView.as_view(), name='details-post'),
]