from django.db import models


class LanguageChoices(models.TextChoices):
    PY = 'py', 'Python'
    JS = 'js', 'JavaScript'
    CPP = 'cpp', 'C++'
    OTHER = 'other', 'Other'