from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory

from posts.choices import LanguageChoices
from posts.models import Post, Comment
from posts.validators import BadLanguageValidator


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        # validators=[
        #     BadLanguageValidator('This text contains bad language!')
        # ],
        widget=forms.TextInput(attrs={
            'class': 'form-control me-2',
            'placeholder': 'Search',
            'type': 'search',
            'aria-label': 'Search',
        })
    )

# class PostForm(forms.Form):
#     title = forms.CharField(max_length=100, widget=forms.TextInput)
#     content = forms.CharField(widget=forms.Textarea())
#     author = forms.CharField(max_length=50)
#     languages = forms.ChoiceField(choices=LanguageChoices.choices)

class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Your title here',
            })
        }

        error_messages = {
            'title': {
                'required': 'The post title is a required field!',
                'max_length': 'The post title is too long!',
                'unique': 'The post title is already taken!',
            },
        }

    def clean_author(self):
        author = self.cleaned_data['author']

        if not author.isalpha():
            raise ValidationError('Author must contain only letters!')

        return author

    def clean(self):
        cleaned_data = super().clean()
        title = self.cleaned_data.get('title')
        content = self.cleaned_data.get('content')

        if title in content:
            raise ValidationError('Title cannot be contained in the content!')

        return cleaned_data

    def save(self, commit=True):
        post = super().save(commit=False)

        post.author = post.author.capitalize()

        if commit:
            post.save()

        return post


class PostCreateForm(PostBaseForm):
    ...

class PostEditForm(PostBaseForm):
    ...

class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['author', 'content']

        labels = {
            'author': '',
            'content': '',
        }

        error_messages = {
            'author': {
                'required': 'The author is a required field!',
            },
            'content': {
                'required': 'The comment is required!',
            }
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs.update({
            'class': 'form-control me-2',
            # 'style': 'display: none;',
            'placeholder': 'Author name here',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control me-2',
            'placeholder': 'Your comment here...',
            'rows': 2,
        })

CommentFormSet = formset_factory(CommentForm, extra=1)