from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from posts.choices import LanguageChoices
from posts.validators import BadLanguageValidator


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[
            BadLanguageValidator("This text contains bad language!")
        ],
    )

    image = models.ImageField(
        upload_to='post_images/',
        blank=True,
        null=True,
    )

    content = models.TextField(
        validators=[
            BadLanguageValidator("This text contains bad language!")
        ],
    )
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    language = models.CharField(
        choices=LanguageChoices.choices,
        default=LanguageChoices.OTHER,
    )

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)