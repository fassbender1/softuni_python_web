from django.db import models

from common.models import TimeStampModel
from destination.models import Destination


class Review(TimeStampModel):
    author = models.CharField(max_length=100)
    body = models.TextField()
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    # created_at = models.DateTimeField(auto_now_add=True)
    destination = models.ForeignKey("destination.Destination", on_delete=models.CASCADE, related_name="reviews")
    is_published = models.BooleanField(default=True)
