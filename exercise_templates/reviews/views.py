from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from reviews.models import Review


# Create your views here.

def review_list(request: HttpRequest) -> HttpResponse:
    reviews_list = Review.objects.all().order_by('author')
    context = {'list_reviews': reviews_list}
    return render(request, 'reviews/list_all.html', context)


def recent_reviews(request: HttpRequest) -> HttpResponse:
    DEFAULT_REVIEW_COUNT = 10
    reviews_count = int(request.GET.get('count', DEFAULT_REVIEW_COUNT))
    reviews = Review.objects.select_related('book')[:reviews_count]

    context = {'reviews': reviews,
               'page_title': 'Recent reviews',
               }

    return render(request, 'reviews/list.html', context)

def review_details(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(
        Review,
        pk=pk
    )

    context = {'review': review, 'page_title': f'{review.author}\'s review on {review.book.title}'}
    return render(request, 'reviews/detail.html', context)
