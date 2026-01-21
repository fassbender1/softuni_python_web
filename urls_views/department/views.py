from django import http
from django.shortcuts import render

# Create your views here.

def index(request: http.HttpRequest, id: int) -> http.HttpResponse:
    return http.HttpResponse(f"The ID is {id}", content_type="text/plain")