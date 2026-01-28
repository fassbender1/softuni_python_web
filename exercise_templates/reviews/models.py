from django.db import models

from books.models import Book
from common.models import TimeStampModel


# Create your models here.


class Review(TimeStampModel):
    author = models.CharField(max_length=100)
    body = models.TextField()
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews") # or "books.Book"
    is_spoiler = models.BooleanField(default=False)

    def update_book_rating(self):
        reviews = self.book.reviews.all()
        self.book.reviews_count = reviews.count()
        if self.book.reviews_count > 0:
            self.book.average_rating = sum([review.rating for review in reviews]) / self.book.reviews_count
        else:
            self.book.average_rating = 0
        self.book.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_book_rating()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.update_book_rating()

    class Meta:
        ordering = ['-created_at']
