from django import forms
from .models import Class
import uuid


def generate_jitsi_id():
    return "webschool/" + uuid.uuid4().hex


class ClassCreateForm(forms.ModelForm):

    class Meta:
        model = Class
        exclude = ('created_by', 'meeting_id')

    def save(self, commit=True):
        instance = super(ClassCreateForm, self).save(commit=False)
        instance.meeting_id = generate_jitsi_id()
        if commit:
            instance.save()
        return instance
