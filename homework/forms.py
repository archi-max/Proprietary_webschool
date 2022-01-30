from django import forms
from .models import Work, Submission
import datetime

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['file']

    def save(self, user, work, commit=True):
        instance = super(SubmissionForm, self).save(commit=False)
        instance.work = work
        instance.student = user

        if instance.work.upload_by < datetime.date.today():
            raise forms.ValidationError("Deadline has passed")

        if commit:
            instance.save()
        return instance



class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'description', 'upload_by', 'groups', 'work_type']

    def clean_upload_by(self):
        date = self.cleaned_data['upload_by']
        if date < datetime.datetime.now():
            raise forms.ValidationError("Date cannot be in the past")

        return date

    def save(self, commit=True):
        instance = super(WorkForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance