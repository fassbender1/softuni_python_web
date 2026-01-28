from django.db import models
from django.utils.text import slugify

from common.models import TimeStampModel


# Create your models here.

class Book(TimeStampModel):
    class GenreChoices(models.TextChoices):
        Fiction = "Fiction", 'Fiction'
        NON_Fiction = "Non-Fiction", 'Non-Fiction'
        Fantasy = "Fantasy", 'Fantasy'
        Science = "Sci-Fi", 'Sci-Fi'
        History = "History", 'History'
        Mystery = "Mystery", 'Mystery'
        Thriller = "Thriller", 'Thriller'


    author = models.CharField(max_length=100, default="")
    title = models.CharField(unique=True, max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isbn = models.CharField(unique=True, max_length=12)
    genre = models.CharField(max_length=50, choices=GenreChoices.choices)
    publishing_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    pages = models.PositiveIntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=100)
    average_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    reviews_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.publisher}")
        super().save(*args, **kwargs)
