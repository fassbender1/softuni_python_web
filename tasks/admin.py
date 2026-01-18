from django.contrib import admin

from tasks import models
from tasks.models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    is_completed = bool

# admin.site.register(Task)   # one way to do it