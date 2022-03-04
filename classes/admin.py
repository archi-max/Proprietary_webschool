from django.contrib import admin
from .models import Class, Event
# Register your models here.

admin.site.register((Class, Event))
