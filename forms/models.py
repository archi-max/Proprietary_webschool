from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group
# Create your models here.

class Form(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, related_name='forms')

class Question(models.Model):
    MCQ = 'MCQ'
    TEXT_FIELD = 'TF'
    TEXT_AREA = 'TA'
    FILE_UPLOAD = 'FU'
    IMAGE_UPLOAD = 'IU'

    QUESTION_TYPES = (
        (MCQ, 'Multiple Choice Question'),
        (TEXT_FIELD, 'Text Field'),
        (TEXT_AREA, 'Text Area'),
        (FILE_UPLOAD, 'File Upload'),
        (IMAGE_UPLOAD, 'Image Upload'),
    )

    form = models.ForeignKey('Form', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    question_number = models.SmallIntegerField()

    # Fields for MCQ
    possible_choices = models.PositiveSmallIntegerField(default=0)
    maximum_choices = models.PositiveSmallIntegerField(default=0)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_possible_choices >= maximum_choices',
                check=models.Q(maximum_choices__lte=models.F("possible_choices")),
            )
        ]


    def __str__(self):
        return self.form.title + ' Q' + str(self.question_number)


