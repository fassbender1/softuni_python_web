from django.urls import path, include

import books
from books.views import landing_page, books_list, book_detail, book_rating, recently_added, book_create, book_edit, \
    book_delete, most_reviewed

app_name = 'books'

books_patterns = [
    path('', books_list, name='list'),
    path('create/', book_create, name='create'),
    path('<slug:slug>', book_detail, name='details'),
    path('top-rated/', book_rating, name='top-rated'),
    path('most-reviewed/', most_reviewed, name='most-reviewed'),
    path('<int:pk>/', include([
        path('edit/', book_edit, name='edit'),
        path('delete/', book_delete, name='delete'),
    ])),
    path('recently-added/', recently_added, name='recently-added'),
]
urlpatterns = [
    path('', landing_page, name='home'),
    path('books/', include(books_patterns)),
]