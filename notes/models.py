from django.db import models
from django.conf import settings
# Create your models here.
import json

initial_data = [
 {
  "id": "kyysw8ccau2pi34yw2c",
  "html": "",
  "tag": "p"
 }
]

def get_data(): return initial_data

class Notebook(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    notebook_id = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)




