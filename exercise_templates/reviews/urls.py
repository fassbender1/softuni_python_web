from django.urls import path, include

from reviews.views import recent_reviews, review_details, review_list, review_create, review_edit, review_delete

app_name = 'reviews'

reviews_patterns = [
    path('recent/', recent_reviews, name='recent'),
    path('<int:pk>/', review_details, name='details'),
    path('', review_list, name='list_all'),
    path('create/', review_create, name='create'),
    path('edit/<int:pk>/', review_edit, name='edit'),
    path('delete/<int:pk>/', review_delete, name='delete'),
]

urlpatterns = [
    path('', include(reviews_patterns)),
]

