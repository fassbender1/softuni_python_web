from django.forms.models import modelformset_factory
from django.urls import reverse_lazy
from django.views import generic

from books.models import Book
from reviews.forms import ReviewCreateForm, ReviewEditForm, ReviewDeleteForm, ReviewFormBasic
from reviews.models import Review


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

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

    context = {
        'reviews': reviews,
        'page_title': 'Recent reviews',
    }

    return render(request, 'reviews/list.html', context)


def review_details(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(
        Review,
        pk=pk
    )

    context = {
        'review': review,
        'page_title': f"{review.author}'s review on {review.book.title}"
    }
    return render(request, 'reviews/detail.html', context)

def review_create(request: HttpRequest) -> HttpResponse:
    form = ReviewFormBasic(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('reviews:recent')

    context = {
        'form': form,
    }
    return render(request, 'reviews/review_create.html', context)

def review_bulk_update(request: HttpRequest, book_slug: str) -> HttpResponse:
    book = get_object_or_404(Book, slug=book_slug)
    ReviewFormSet = modelformset_factory(
        Review,
        form=ReviewEditForm,
        can_delete=True,
        extra=1,
    )
    formset = ReviewFormSet(
        request.POST or None,
        queryset=Review.objects.filter(book=book),
    )

    if request.method == 'POST' and formset.is_valid():
        instances = formset.save(commit=False)
        for instance in instances:
            instance.book = book
            instance.save()
        for instance in formset.deleted_objects:
            instance.delete()
        return redirect('reviews:list_all')

    context = {
        "formset": formset,
        "book": book,
    }

    return render(request, 'reviews/formset-edit.html', context)

def review_edit(request: HttpRequest, pk: int) -> HttpResponse:
    review = Review.objects.get(pk=pk)
    form = ReviewEditForm(request.POST or None, instance=review)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('reviews:list_all')

    context = {
        'form': form,
    }
    return render(request, 'reviews/review_edit.html', context)

def review_delete(request: HttpRequest, pk: int) -> HttpResponse:
    review = Review.objects.get(pk=pk)
    form = ReviewDeleteForm(request.POST or None, instance=review)

    if request.method == 'POST' and form.is_valid():
        review.delete()
        return redirect('reviews:list_all')

    context = {
        'form': form,
    }
    return render(request, 'reviews/review_delete.html', context)

# class ReviewCreateView(generic.CreateView):
#     model = Review
#     form_class = ReviewCreateForm
#     template_name = 'reviews/review_create.html'
#     success_url = reverse_lazy('reviews:list_all')
#
#
# class ReviewUpdateView(generic.UpdateView):
#     model = Review
#     form_class = ReviewEditForm
#     template_name = 'reviews/review_edit.html'
#     success_url = reverse_lazy('reviews:list_all')
#
#
# class ReviewDeleteView(generic.DeleteView):
#     model = Review
#     form_class = ReviewDeleteForm
#     template_name = 'reviews/review_delete.html'
#     success_url = reverse_lazy('reviews:list_all')
#
#
# class ReviewListView(generic.ListView):
#     model = Review
#     template_name = 'reviews/review_list.html'
#     context_object_name = 'reviews'