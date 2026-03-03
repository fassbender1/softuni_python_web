from django import http
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from department.models import Department


# Create your views here.

def index(request: http.HttpRequest, pk: int) -> http.HttpResponse:
    # department = get_object_or_404(Department, pk=pk)
    # return render(request, 'index.html', {'department': department})
    # return http.HttpResponse(f"The type is {type(id)}", content_type="text/plain")
    return HttpResponseForbidden()

def redirect_view(request: http.HttpRequest) -> http.HttpResponse:
    # return index(request) # bad because no actual redirect
    # return redirect('http://127.0.0.1:8000/')  # bad because we hard code the url
    # return redirect("/") # better but not perfect
    return redirect("home", pk=2)

def slug_view(request: http.HttpRequest, slug: str) -> http.HttpResponse:
    return http.HttpResponse(f"The type is {type(slug)} and the slug is {slug}", content_type="text/plain")

def path_view(request: http.HttpRequest, path: str) -> http.HttpResponse:
    return http.HttpResponse(f"The type is {type(path)} and the path is {path}", content_type="text/plain")

def uuid_view(request: http.HttpRequest, uuid: str) -> http.HttpResponse:
    return http.HttpResponse(f"The type is {type(uuid)} and the uuid is {uuid}", content_type="text/plain")

def show_archive(request: http.HttpRequest, archive_year: int) -> http.HttpResponse:
    return http.HttpResponse(f"the requested year is {archive_year}")