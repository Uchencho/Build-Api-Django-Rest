from django.contrib import admin
from .forms import StatusForm

# Register your models here.
from . models import Status


class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'image']
    form = StatusForm

admin.site.register(Status, StatusAdmin)