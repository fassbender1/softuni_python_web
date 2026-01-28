from django.urls import path, include

from reviews.views import recent_reviews, review_details, review_list

app_name = 'reviews'
reviews_patterns = [
    path('recent/', recent_reviews, name='recent'),
    path('<int:pk>/', review_details, name='details'),
    path('', review_list, name='list_all'),
]

urlpatterns = [
    path('', include(reviews_patterns))
]