from django.db import models
from django.contrib.auth.models import Group
from django.conf import settings
from forms.models import FileBaseResponse
# Create your models here.
from utils.files import filename_generator, document_fileextension_validator as dfv


def class_filename_generator(instance, filename):
    print("subclass method")
    return filename_generator(instance, filename, "submissions")

class Work(models.Model):
    PRACTICAL = 'PR'
    HOMEWORK = 'HW'

    WORK_TYPE_CHOICES = (
        (PRACTICAL, 'Practical'),
        (HOMEWORK, 'Homework'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    groups = models.ManyToManyField(Group)
    upload_by = models.DateTimeField(auto_now_add=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    work_type = models.CharField(max_length=2, choices=WORK_TYPE_CHOICES, default=HOMEWORK)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# def submission_filename_generator(instance, filename):
#     print("subclass method")
#     return filename_generator(instance, filename, "submissions")


class Submission(FileBaseResponse):
    class_validators = [dfv]
    folder_name = "submissions"
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.get_full_name() + " - " + self.work.title
