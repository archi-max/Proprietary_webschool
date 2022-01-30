from django.db import models
import uuid
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib.auth.models import Group
from utils.files import filename_generator as fg, document_fileextension_validator

def filename_generator(inst, fn):
    return fg(inst, fn, 'posts')

class Post(models.Model):

    ANNOUNCEMENT = 'AN'
    RESULT = 'RS'
    QUESTION_BANK = 'QB'
    NOTES = 'NT'

    TYPE_CHOICES = (
        (ANNOUNCEMENT, 'Announcement'),
        (RESULT, 'Result'),
        (QUESTION_BANK, 'Question Bank'),
        (NOTES, 'Notes'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    file = models.FileField(upload_to=filename_generator, validators=[document_fileextension_validator], blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name='posts')
    tags = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=True, default=ANNOUNCEMENT)
    groups = models.ManyToManyField(Group, blank=True, related_name='posts') # groups that can see this announcement

    def __str__(self):
        return self.title