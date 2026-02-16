from django.db.models import Avg
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from destinations.forms import DestinationForm
from destinations.models import Destination


# Create your views here.
class DestinationCreateView(CreateView):
    # queryset = Traveler.objects.all()
    model = Destination
    form_class = DestinationForm
    success_url = reverse_lazy('common:home')

class DestinationDetailView(DetailView):
    # model = Destination  # - same as just with the queryset line, but the travelers, reviews will not be refreshed
    queryset = Destination.objects.prefetch_related('travelers', 'reviews').annotate(
            avg_rating=Avg('reviews__rating')
        )
    # def get_queryset(self):
    #     return Destination.objects.prefetch_related('travelers', 'reviews')  # - same as just with the queryset line
