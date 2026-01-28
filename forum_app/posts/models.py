from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)