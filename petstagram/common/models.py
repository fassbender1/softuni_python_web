from django.contrib.auth.models import User
from django.db import models

from photos.models import Photo


# Create your models here.

class Model(models.Model):
    text = models.CharField(max_length=300)
    date_and_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)