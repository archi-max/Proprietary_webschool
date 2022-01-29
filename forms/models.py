from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group
from utils.files import filename_generator, document_fileextension_validator as extension_validator
# Create your models here.

answer_filename_generator = lambda instance, filename: filename_generator(instance, filename, 'forms\\answers')
question_filename_generator = lambda instance, filename: filename_generator(instance, filename, 'forms\\questions')

class Form(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, related_name='forms')
    maximum_responses = models.PositiveSmallIntegerField(default=1)

class Question(models.Model):

    TEXT_FIELD = 'TF'
    TEXT_AREA = 'TA'
    FILE_UPLOAD = 'FU'
    IMAGE_UPLOAD = 'IU'
    MCQ = 'MC'

    QUESTION_TYPES = (
        (MCQ, 'Multiple Choice Question'),
        (TEXT_FIELD, 'Text Field'),
        (TEXT_AREA, 'Text Area'),
        (FILE_UPLOAD, 'File Upload'),
        (IMAGE_UPLOAD, 'Image Upload'),
    )

    form = models.ForeignKey('Form', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=question_filename_generator, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=QUESTION_TYPES, default=TEXT_FIELD, blank=True)
    question_number = models.SmallIntegerField()

    #MCQ
    choices = models.TextField(null=True, blank=True)  # Choices are separated by commas
    multiple_answer = models.BooleanField(default=False, blank=True)

    #TODO: Add constraint to make sure image or text is not null

    def __str__(self):
        return self.form.title + ' Q' + str(self.question_number)


class ResponseSheet(models.Model):
    form = models.ForeignKey('Form', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BaseResponse(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    # TODO: Add constraint to make sure image or text is not null
    def __str__(self):
        return self.user.get_full_name() + ' ' + self.form.title


class FileBaseResponse(BaseResponse):
    class_filename_generator = answer_filename_generator
    class_validators = []
    file = models.FileField(upload_to=class_filename_generator, blank=True, validators=class_validators)


class ImageBaseResponse(BaseResponse):
    class_filename_generator = answer_filename_generator
    class_validators = []
    image = models.ImageField(upload_to=class_filename_generator, blank=True)


class TextBaseResponse(BaseResponse):
    class_validators = []
    text = models.TextField(blank=True, validators=class_validators) # Multiple Answers will have a list of answers seperated by a comma


class CombinedBaseResponse(BaseResponse):
    class_filename_generators = {
        "file": answer_filename_generator,
        "image": answer_filename_generator,
    }
    class_validators = {
        "file": [],
        "image": [],
        "text": [],
    }

    file = models.FileField(upload_to=class_filename_generators["file"], blank=True, validators=class_validators["file"])
    image = models.ImageField(upload_to=class_filename_generators["image"], blank=True, validators=class_validators["image"])
    text = models.TextField(blank=True, validators=class_validators["text"])


class FileResponse(FileBaseResponse):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer_key = models.ForeignKey(ResponseSheet, on_delete=models.CASCADE, related_name='file_answers')


class ImageResponse(ImageBaseResponse):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer_key = models.ForeignKey(ResponseSheet, on_delete=models.CASCADE, related_name='image_answers')


class TextResponse(TextBaseResponse):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer_key = models.ForeignKey(ResponseSheet, on_delete=models.CASCADE, related_name='text_answers')


class CombinedResponse(CombinedBaseResponse):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_key = models.ForeignKey(ResponseSheet, on_delete=models.CASCADE, related_name='combine_answers')