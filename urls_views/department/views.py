from django import http
from django.shortcuts import render

# Create your views here.

def index(request: http.HttpRequest) -> http.HttpResponse:
    return http.HttpResponse("Hello, world. You're the department!", content_type="text/plain")