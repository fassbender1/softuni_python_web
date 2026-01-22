from django.urls import path

from review.views import recent_reviews, review_detail

app_name = 'review'
urlpatterns = [
    path('', recent_reviews, name='list'),
    path('details/<int:pk>/', review_detail, name='detail'),
]