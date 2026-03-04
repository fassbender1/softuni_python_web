from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


# Create your views here.

class HomeView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'fbv/home.html'
    # permission_required = 'view_session'   # example as the bobi2 user was edited to only be able to view users
    permission_required = 'auth.view_user'   # example, bobi2 can view only user data, so this works

@login_required
def home(request):
    return render(request, 'fbv/home.html')
    # if request.user.has_perm('view_session'):     # FBV example on limiting a user that doesn't have permissions, to 403 error page, instead of home, if he does have permission
    #     return render(request, 'fbv/home.html')
    #
    # return HttpResponse(status=403)

def register_fbv(request: HttpRequest):
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')

    return render(request, 'fbv/register.html', {'form': form})

def login_fbv(request: HttpRequest) -> HttpResponse:
    form = AuthenticationForm(request, request.POST or None)

    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('home')


    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # user = authenticate(request, username=username, password=password)
    #
    # if user:
    #     login(request, user)
    #     return redirect('home')

    return render(request, 'fbv/login.html', {'form': form})

def logout_fbv(request: HttpRequest):
    if request.POST:
        logout(request)
    return redirect('home')



