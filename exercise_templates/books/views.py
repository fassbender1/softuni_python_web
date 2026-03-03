from django.db.models import Avg, Q
from django.forms.models import modelform_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from books.forms import BookFormBasic, BookEditForm, BookDeleteForm, BookSearchForm
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
    most_reviews = Book.objects.order_by('-reviews_count')[:3]

    context = {
        'total_books': total_books,
        'latest_book': latest_book,
        'page_title': 'Landing page',
        'top_books': top_books,
        'latest_review': latest_review,
        'latest_review_author': latest_review_author,
        'latest_review_rating': latest_review_rating,
        'most_reviews': most_reviews,
    }
    return render(request, 'books/landing_page.html', context)

def books_list(request: HttpRequest) -> HttpResponse:
    search_form = BookSearchForm(request.GET or None)

    list_books = Book.objects.annotate(
        avg_rating=Avg('reviews__rating')
    ).order_by('title')

    if 'query' in request.GET:
        if search_form.is_valid():
            search_value = search_form.cleaned_data['query']
            list_books = list_books.filter(
                Q(title__icontains=search_value)
                    |
                Q(description__icontains=search_value)
            )

    context = {
        'books': list_books,
        'page_title': 'Dashboard',
        'search_form': search_form,
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

def most_reviewed(request: HttpRequest) -> HttpResponse:
    list_most_reviewed = Book.objects.order_by('-reviews_count')[:10]
    context = {
        'most_reviewed_list': list_most_reviewed,
    }

    return render(request, 'books/most_reviewed.html', context)

def book_create(request: HttpRequest) -> HttpResponse:
    # BookForm = modelform_factory(Book, exclude=('slug',)) - to make it work with modelform factory
    # form = BookForm(request.POST or None)
    form = BookFormBasic(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        # Book.objects.create(
        #     **form.cleaned_data,
        #     # title=form.cleaned_data['title'],
        #     # publishing_date=form.cleaned_data['publishing_date'],
        #     # isbn=form.cleaned_data['isbn'],
        #     # price=form.cleaned_data['price'],
        #     # genre=form.cleaned_data['genre'],
        #     # description=form.cleaned_data['description'],
        #     # image_url=form.cleaned_data['image_url'],
        #     # publisher=form.cleaned_data['publisher'],
        #
        # )
        form.save()
        return redirect('books:home')

    context = {
        'form': form,
    }
    return render(request, 'books/create.html', context)

def book_edit(request: HttpRequest, pk: int) -> HttpResponse:
    book = Book.objects.get(pk=pk)
    form = BookEditForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('books:home')

    context = {
        'form': form,
    }
    return render(request, 'books/edit.html', context)

def book_delete(request: HttpRequest, pk: int) -> HttpResponse:
    book = Book.objects.get(pk=pk)
    form = BookDeleteForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():
        book.delete()
        return redirect('books:home')

    context = {
        'form': form,
    }
    return render(request, 'books/delete.html', context)