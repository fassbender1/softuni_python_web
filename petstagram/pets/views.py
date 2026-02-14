from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def pet_add(request: HttpRequest) -> HttpResponse:
    return render(request, 'pets/pet-add-page.html')

def pet_details(request: HttpRequest, username: str, pet_slug:str) -> HttpResponse:
    return render(request, 'pets/pet-details-page.html')

def pet_edit(request: HttpRequest, username: str, pet_slug:str) -> HttpResponse:
    return render(request, 'pets/pet-edit-page.html')

def pet_delete(request: HttpRequest, username: str, pet_slug:str) -> HttpResponse:
    return render(request, 'pets/pet-delete-page.html')