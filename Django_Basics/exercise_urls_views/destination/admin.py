from django.contrib import admin

from destination.models import Destination


# Register your models here.

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    ...