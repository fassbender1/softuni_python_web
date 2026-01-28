from django.db.models import Avg
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from books.models import Book
from reviews.models import Review


# Create your views here.

def landing_page(request: HttpRequest) -> HttpResponse:
    total_books = Book.objects.count()
    latest_book = Book.objects.order_by('-publishing_date').first()
    top_books = Book.objects.order_by('-average_rating')[:3]
    latest_review = (
        Review.objects
        .select_related('book')
        .order_by('-created_at')
        .first()
    )
    latest_review_author = latest_review.author
    latest_review_rating = latest_review.rating

    context = {
        'total_books': total_books,
        'latest_book': latest_book,
        'page_title': 'Landing page',
        'top_books': top_books,
        'latest_review': latest_review,
        'latest_review_author': latest_review_author,
        'latest_review_rating': latest_review_rating,
    }
    return render(request, 'books/landing_page.html', context)

def books_list(request: HttpRequest) -> HttpResponse:
    list_books = Book.objects.annotate(
        avg_rating=Avg('reviews__rating')
    ).order_by('title')

    context = {
        'books': list_books,
        'page_title': 'Dashboard',
    }

    return render(request, 'books/list.html', context)

def book_detail(request: HttpRequest, slug: str) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)
    reviews = book.reviews.all()

    context = {
        'book': book,
        'reviews': reviews,
        'average_rating': book.average_rating,
        'reviews_count': book.reviews_count,
        'page_title': f'{book.title} details',
    }

    return render(request, 'books/detail.html', context)

def book_rating(request: HttpRequest) -> HttpResponse:
    list_top_books = Book.objects.order_by('-average_rating')[:10]

    context = {
        'top_books_list': list_top_books,
    }

    return render(request, 'books/top_rated.html', context)

def recently_added(request: HttpRequest) -> HttpResponse:
    list_recent_books = Book.objects.order_by('-publishing_date')[:10]
    context = {
        'recent_books_list': list_recent_books,
    }

    return render(request, 'books/recently_added.html', context)