from django.db import models
# Create your models here.
from utils.files import filename_generator, document_fileextension_validator as dfv
from django.conf import settings
from datetime import timedelta
from django.contrib.auth.models import Group
from forms.models import FileBaseResponse


class WrittenExam(models.Model):
    duration = models.DurationField()
    starts_at = models.DateTimeField()
    exam_name = models.CharField(max_length=100)
    uploading_time = models.DurationField(default=timedelta(minutes=15))
    question_paper = models.FileField(upload_to=filename_generator, validators=[dfv])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='exams_created')
    groups = models.ManyToManyField(Group, related_name='exams')

    def __str__(self):
        return self.exam_name


class AnswerKey(FileBaseResponse):
    class_validators = [dfv]
    folder_name = 'exams'
    exam = models.ForeignKey(WrittenExam, on_delete=models.CASCADE, related_name='answer_keys')
    answered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='answer_keys')

    def __str__(self):
        return self.answered_by.get_full_name() + ' ' + self.exam.exam_name
