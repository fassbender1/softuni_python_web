from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from common.mixins import AgeRestrictionMixin
from reviews.forms import ReviewForm
from reviews.models import Review, REVIEW_TYPE_CHOICES


# Create your views here.

# @method_decorator(login_required, name='dispatch')   # second way to make sure review creation can be only for specific age checks
class ReviewCreateView(AgeRestrictionMixin, CreateView):   # one way to make sure the review creation can only be done for specific age checks : LoginRequiredMixin,
    # queryset = Traveler.objects.all()
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('common:home')

class ReviewListView(ListView):
    ordering = '-created_at'
    paginate_by = 2

    def get_paginate_by(self, queryset):                      # add the option for users to create the number to paginate_by on each page, select how many reviews to show per page
        per_page_param = self.request.GET.get('per_page')        # ?per_page=10, to test with: http://127.0.0.1:8000/reviews/?page=1&per_page=3
        if per_page_param:
            try:
                return int(per_page_param)
            except (TypeError, ValueError):
                pass
        return super().get_paginate_by(queryset)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_messages'] = f"You are on page: {context['page_obj'].number}"
        return context

    def get_queryset(self) -> QuerySet[Review]:
        qs = Review.objects.filter(is_verified=True)
        review_type = self.request.GET.get('type')

        if review_type:
            if review_type not in REVIEW_TYPE_CHOICES.labels:
                raise HttpResponseBadRequest

            qs = qs.filter(review_type=review_type)

        return qs