from django.db import models
from django.conf import settings
# Create your models here.
import json

initial_data = {"blocks":[
 {
  "id": "kyysw8ccau2pi34yw2c",
  "html": "",
  "tag": "p"
 }
]}

def get_data(): return initial_data

class Notebook(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data = models.TextField(default=initial_data, unique=False)

