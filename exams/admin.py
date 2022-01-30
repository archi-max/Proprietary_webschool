from django.contrib import admin
from .models import WrittenExam, AnswerKey
# Register your models here.

admin.site.register([WrittenExam, AnswerKey])

