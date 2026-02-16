

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.timezone import now
from django.views import View
from django.views.generic import TemplateView, RedirectView

from travelers.models import Traveler


# Create your views here.

class Welcome(View):
    # def dispatch(self, request, *args, **kwargs): # in case that you need to overwrite the dispatch
    #     if request.user.is_staff:
    #         return HttpResponse(status=403)
    #     return super().dispatch(request, *args, **kwargs)

    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Welcome to our travel app!")

    def post(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Post was called!")

class HomeView(TemplateView):

    def get_context_data(self, **kwargs):
        kwargs.update({
            "current_time": str(now()),
            "travelers_count": Traveler.objects.count(),
        })
        return super().get_context_data(**kwargs)

    def get_template_names(self) -> list:
        if self.request.user.is_staff:
            return ['admin_home.html']
        return ['home.html']

class HomeTeenWelcomeView(TemplateView):
    template_name = "teen_welcome.html"

class AgeCheckRedirectView(RedirectView):
    permanent = False # comes by default
    # url = 'http://127.0.0.1:8000/home/' # bad idea but will work
    # url = 'home/' # still a bad idea but better than above
    # pattern_name = 'common:home'  # good, but not the best - below is the best option

    def get_redirect_url(self, *args, **kwargs) -> str:
        traveler = None
        pk = self.request.GET.get('pk')
        # traveler = Traveler.objects.get(pk=pk)
        traveler = get_object_or_404(Traveler, pk=pk)
        if traveler.age > 21:
            return reverse('common:home')
        return reverse('common:home-teen')
