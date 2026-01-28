from django.contrib import admin

from reviews.models import Review


# Register your models here.

@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['book__title', 'rating']