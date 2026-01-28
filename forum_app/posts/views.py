import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")

def dashboard(request: HttpRequest) -> HttpResponse:
    context = {
        'posts':  [
            {
            'title': 'This is a test post 1',
            'content': '',
            'author': 'Boris',
            'created_at': datetime.datetime.now(),
            },
            {
            'title': 'This is a test post 2',
            'content': '*Some* Description here',
            'author': 'Pesho',
            'created_at': datetime.datetime.now(),
            },
            {
             'title': 'This is a test post 3',
            'content': '**Some** <i>Description</i> here',
            'author': 'Gosho',
            'created_at': datetime.datetime.now(),
            },
        ],
    }

    return render(request, 'dashboard.html', context)