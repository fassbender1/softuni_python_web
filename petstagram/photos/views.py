from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from photos.models import Photo


# Create your views here.

def photo_add(request: HttpRequest) -> HttpResponse:
    return render(request, 'photos/photo-add-page.html')

def photo_details(request: HttpRequest, pk: int) -> HttpResponse:
    photo = Photo.objects.prefetch_related('tagged_pets', 'like_set', 'comment_set').get(pk=pk)

    context = {
        'photo': photo,
    }

    return render(request, 'photos/photo-details-page.html', context)

def photo_edit(request: HttpRequest, pk:int) -> HttpResponse:
    return render(request, 'photos/photo-edit-page.html')