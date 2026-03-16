from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):   # PermissionRequiredMixin needed for below commented sections to work
    template_name = 'home.html'
    # permission_required = 'view_session'   # example as the bobi2 user was edited to only be able to view users
    # permission_required = 'auth.view_user'   # example, bobi2 can view only user data, so this works
