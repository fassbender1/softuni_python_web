import datetime
from random import choices
from typing import Any

from django import forms
from django.core.exceptions import ValidationError

from books.models import Book, Tag


# class BookFormBasic(forms.Form):
#      title = forms.CharField(
#          max_length=100,
#          widget=forms.TextInput(attrs={'placeholder': 'e.g. Done'})
#      )
#
#      author = forms.CharField(
#          max_length=50,
#      )
#
#      price = forms.DecimalField(
#          max_digits=6,
#          decimal_places=2,
#          min_value=0,
#          widget=forms.NumberInput(attrs={'step': '2'}),
#          label='Price (EUR)'
#      )
#      isbn = forms.CharField(
#          max_length=12,
#          min_length=10,
#      )
#      genre = forms.ChoiceField(
#          choices=Book.GenreChoices.choices,
#          widget=forms.Select()
#      )
#
#      publishing_date = forms.DateField(
#          initial=datetime.date.today,
#      )
#
#      description = forms.CharField(
#          widget=forms.Textarea(),
#      )
#
#      image_url = forms.URLField()
#
#      publisher = forms.CharField(
#          max_length=100,
#      )


class BookFormBasic(forms.ModelForm):
    tags = forms.CheckboxSelectMultiple()

    class Meta:
        exclude = ['slug', 'reviews_count', 'average_rating']
        # fields = ['title', ]
        model = Book
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'publishing_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        error_messages = {
            'title': {
                'max_length': "The title is too long",
                'required': "The title is required",
            }
        }

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']

        if self.cleaned_data['isbn'].startswith('978'):
            raise ValidationError('ISBN cannot start with 978')

        return isbn

    def clean(self):
        cleaned = super().clean()
        genre = cleaned.get('genre')
        pages = cleaned.get('pages')

        if pages < 10 and genre == Book.GenreChoices.FICTION:
            raise ValidationError(f"Book of type {Book.GenreChoices.FICTION} cannot be less than 10 pages long.")

        return cleaned


    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.all()


class BookCreateForm(BookFormBasic):
    ...

class BookEditForm(BookFormBasic):
    ...

class BookDeleteForm(BookFormBasic):
    # class Meta(BookFormBasic.Meta):
    #     widgets = {
    #         'author': forms.TextInput(attrs={'disabled': True}),
    #     }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].disabled = True

class BookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False,

    )