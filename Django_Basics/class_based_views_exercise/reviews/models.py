from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from travelers.models import Traveler
from destinations.models import Destination

REVIEW_TYPE_CHOICES = (
    ("TEXT", "Text"),
    ("VIDEO", "Video"),
    ("AUDIO", "Audio"),
)

class Review(models.Model):
    body = models.TextField(
        null=False,
        blank=False,
    )
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(0.00),
            MaxValueValidator(5.00)
        ],
        null=False,
        blank=False,
    )
    is_verified = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    review_type = models.CharField(
        max_length=10,
        choices=REVIEW_TYPE_CHOICES,
        default="TEXT",
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
    )

    traveler = models.ForeignKey(
        Traveler,
        on_delete=models.CASCADE,
        related_name='reviews',
        null=False,
        blank=False,
    )
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name='reviews',
        null=False,
        blank=False,
    )

    def clean(self) -> None:
        if self.destination_id and not self.destination.is_available:
            raise ValidationError("Cannot create a review for an unavailable destination")

    def __str__(self):
        return f"Review by {self.traveler.name} for {self.destination.name}"

    class Meta:
        ordering = ('-created_at',)
