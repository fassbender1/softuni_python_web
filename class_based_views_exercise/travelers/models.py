from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from django.forms import ValidationError

from common.choices import CountryChoice
from travelers.validator import validate_email_domain


class Traveler(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        unique=True,
        validators=[validate_email_domain],
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18)],
        null=False,
        blank=False,
    )
    country = models.CharField(
        max_length=20,
        choices=CountryChoice.choices,
        default="OTHER",
        null=False,
        blank=False,
    )
    registered_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-registered_at',)
