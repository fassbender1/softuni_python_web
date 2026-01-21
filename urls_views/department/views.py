from django import http
from django.shortcuts import render

# Create your views here.

def index(request: http.HttpRequest) -> http.HttpResponse:

    return render(request, 'index.html')
    return http.HttpResponse(f"The type is {type(id)}", content_type="text/plain")

def redirect_view(request: http.HttpRequest) -> http.HttpResponse:
    return index(request)

def slug_view(request: http.HttpRequest, slug: str) -> http.HttpResponse:
    return http.HttpResponse(f"The type is {type(slug)} and the slug is {slug}", content_type="text/plain")

def path_view(request: http.HttpRequest, path: str) -> http.HttpResponse:
    return http.HttpResponse(f"The type is {type(path)} and the path is {path}", content_type="text/plain")

def uuid_view(request: http.HttpRequest, uuid: str) -> http.HttpResponse:
    return http.HttpResponse(f"The type is {type(uuid)} and the uuid is {uuid}", content_type="text/plain")

def show_archive(request: http.HttpRequest, archive_year: int) -> http.HttpResponse:
    return http.HttpResponse(f"the requested year is {archive_year}")