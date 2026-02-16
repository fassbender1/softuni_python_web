from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from travelers.forms import TravelerForm
from travelers.models import Traveler


# Create your views here.

class TravelerCreateView(CreateView):
    # queryset = Traveler.objects.all()
    model = Traveler
    form_class = TravelerForm
    success_url = reverse_lazy('common:home')
    # template_name = 'travelers/traveler_form.html' # comes by default

    def form_valid(self, form):
        messages.success(self.request, 'Traveler successfully created')
        return super().form_valid(form)

class TravelerUpdateView(UpdateView):
    model = Traveler
    form_class = TravelerForm
    success_url = reverse_lazy('common:home')

class TravelerDeleteView(DeleteView):   # example how to create this without form
    model = Traveler
    # form_class = TravelerForm
    success_url = reverse_lazy('common:home')

class TravelerDetailView(DetailView):
    template_name = 'travelers/traveler_detail.html' # not required
    model = Traveler
    # context_object_name = 'traveler'
    # queryset = Traveler.objects.all()

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data()
        context['reviews_count'] = self.object.reviews.count()
        context['visited_destinations'] = self.object.destinations
        return context

class TravelerListView(ListView):
    ...
