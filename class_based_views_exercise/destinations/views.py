from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from destinations.forms import DestinationForm
from destinations.models import Destination


# Create your views here.
class DestinationCreateView(CreateView):
    # queryset = Traveler.objects.all()
    model = Destination
    form_class = DestinationForm
    success_url = reverse_lazy('common:home')