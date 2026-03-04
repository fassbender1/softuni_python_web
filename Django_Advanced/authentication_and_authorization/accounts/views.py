from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


# Create your views here
# @login_required
# def home(request):
#     return render(request, 'fbv/home.html')
#     # if request.user.has_perm('view_session'):     # FBV example on limiting a user that doesn't have permissions, to 403 error page, instead of home, if he does have permission
#     #     return render(request, 'fbv/home.html')
#     #
#     # return HttpResponse(status=403)

UserModel = get_user_model()

def register_fbv(request: HttpRequest):
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')

    return render(request, 'accounts/register.html', {'form': form})

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

    return render(request, 'accounts/login.html', {'form': form})

def logout_fbv(request: HttpRequest):
    if request.POST:
        logout(request)
    return redirect('home')

class RegisterView(UserPassesTestMixin, CreateView):
    form_class = UserCreationForm
    model = UserModel
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return not self.request.user.is_authenticated



#LoginRequiredMixin
class ProfileView(TemplateView):
    template_name = "accounts/profile_details.html"

