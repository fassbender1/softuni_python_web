from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from common.forms import CommentForm
from common.models import Like
from photos.models import Photo


# Create your views here.

def home_page(request: HttpRequest) -> HttpResponse:
    all_photos = Photo.objects.prefetch_related('tagged_pets', 'like_set')

    context = {'all_photos': all_photos}

    return render(request, 'common/home-page.html', context)

def add_comment(request: HttpRequest, photo_pk: int) -> HttpResponse:
    if request.method == "POST":
        photo = Photo.objects.get(pk=photo_pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META.get('HTTP_REFERER') + f'#{photo_pk}')

def like_functionality(request: HttpRequest, photo_pk: int) -> HttpResponse:
    like_object = Like.objects.filter(to_photo_id=photo_pk).first()

    if like_object:
        like_object.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_pk,
        )

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_pk}')

def share_functionality(request, photo_pk: int) -> HttpResponse:
    # this will work only on localhost as it copies values on the server
    copy(request.META.get('HTTP_REFERER')[:-1] + resolve_url('photos:details', photo_pk))
    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_pk}')

