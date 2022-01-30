from django.contrib import admin
from .models import Work, Submission
# Register your models here.

admin.site.register((Work, Submission))
