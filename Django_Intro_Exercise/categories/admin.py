from categories.models import Category
from django.contrib import admin

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...