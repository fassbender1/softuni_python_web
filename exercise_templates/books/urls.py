from django.urls import path, include

import books
from books.views import landing_page, books_list, book_detail, book_rating, recently_added

app_name = 'books'

books_patterns = [
    path('', books_list, name='list'),
    path('<slug:slug>', book_detail, name='details'),
    path('top-rated/', book_rating, name='top-rated'),
    path('recently-added/', recently_added, name='recently-added'),
]
urlpatterns = [
    path('', landing_page, name='home'),
    path('books/', include(books_patterns)),
]