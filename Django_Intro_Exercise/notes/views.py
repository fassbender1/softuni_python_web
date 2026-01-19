from django.http import HttpResponse
from django.shortcuts import render

from notes.models import Note


# Create your views here.

def dashboard(request) -> HttpResponse:
    notes = Note.objects.prefetch_related('category').all()

    context = {
        'notes': notes
    }

    return render(request, 'index.html', context)