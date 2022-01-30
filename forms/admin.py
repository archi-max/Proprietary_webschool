from django.contrib import admin
from .models import Question, ResponseSheet, Form, FileResponse, TextResponse, ImageResponse, CombinedResponse
# Register your models here.
models = [Question, ResponseSheet, Form, FileResponse, TextResponse, ImageResponse, CombinedResponse]
admin.site.register(models)
