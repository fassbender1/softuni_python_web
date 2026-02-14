from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify

from books.validators import range_validator2, RangeValidator
from common.models import TimeStampModel


# Create your models here.

class Book(TimeStampModel):
    class GenreChoices(models.TextChoices):
        FICTION = 'Fiction', 'Fiction'
        NON_FICTION = 'Non-Fiction', 'Non-Fiction'
        FANTASY = 'Fantasy', 'Fantasy'
        SCIENCE = 'Sci-Fi', 'Sci-Fi'
        HISTORY = 'History', 'History'
        MYSTERY = 'Mystery', 'Mystery'
        THRILLER = 'Thriller', 'Thriller'



    author = models.CharField(max_length=100, default="")
    title = models.CharField(unique=True, max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[
        # range_validator2(0, 100),
        RangeValidator(0, 1000, message="Price must be between 0 and 1000"),
    ])
    isbn = models.CharField(unique=True, max_length=12)
    cover_image = models.ImageField(null=True, blank=True)
    genre = models.CharField(max_length=50, choices=GenreChoices.choices)
    publishing_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    pages = models.PositiveIntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=100)
    average_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    reviews_count = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(
        "Tag"
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.publisher}")
        super().save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(
        max_length=50,

    )

    books = models.ManyToManyField(
        Book,
    )

    def __str__(self):
        return self.name