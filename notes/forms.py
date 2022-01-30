from django import  forms
from .models import Notebook
import json
import requests


def create_notion_page():
    url = 'http://localhost:8080/pages/'
    data = {"blocks": [{"tag": "h1", "html": "Notebook Title", "imageUrl": ""}]}
    headers = {"Content-Type": "application/json"}
    res = requests.post(url, json=data, headers=headers)
    res = json.loads(res.text)
    return res['pageId']


class NotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = ['title']

    def save(self, commit=True):
        notebook = super(NotebookForm, self).save(commit=False)
        notebook.notebook_id = create_notion_page()
        if commit:
            notebook.save()
        return notebook
