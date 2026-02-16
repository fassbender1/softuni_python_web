from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator

from common.choices import CountryChoice
from travelers.models import Traveler


class Destination(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    country = models.CharField(
        max_length=10,
        choices=CountryChoice.choices,
        default="OTHER",
        null=False,
        blank=False,
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0.00)],
        null=False,
        blank=False,
    )
    is_available = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        unique=True,
        editable=False,
        max_length=100,
        null=False,
        blank=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False,
    )

    travelers = models.ManyToManyField(
        Traveler,
        related_name='destinations',
        blank=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'country'],
                name='unique_destination_per_country',
            )
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.country}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-updated_at',)
