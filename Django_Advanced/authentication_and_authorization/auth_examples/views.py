from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

@login_required
def home(request):
    return render(request, 'fbv/home.html')

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



