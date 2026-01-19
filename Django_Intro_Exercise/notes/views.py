from django.http import HttpResponse
from django.shortcuts import render

from notes.models import Note


# Create your views here.

def dashboard(request) -> HttpResponse:
    return HttpResponse("This is my first View!")