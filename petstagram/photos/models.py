from django.core.validators import FileExtensionValidator, MinLengthValidator
from django.db import models

from pets.models import Pet
from photos.validators import FileSizeValidator


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(validators=[FileSizeValidator(5)])
    description = models.CharField(max_length=100, validators=[MinLengthValidator(10)], null=True, blank=True)
    location = models.CharField(max_length=30)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)

