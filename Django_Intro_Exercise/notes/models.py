from django.db import models

# Create your models here.
class Note(models.Model):
    # class PriorityChoices(models.IntegerChoices):
    #     LOW = 1, 'Low'
    #     MEDIUM = 2, 'Medium'
    #     HIGH = 3, 'High'

    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    # priority = models.PositiveIntegerField(choices=PriorityChoices, default=PriorityChoices.LOW)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
