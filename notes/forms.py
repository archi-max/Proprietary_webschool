from django import  forms
from .models import Notebook, NotebookDatabase
import json
import requests
import os
import re

def dbid_from_url(url):
    return re.match("https://www.notion.so/(.+?)?v=.+?", url)[1][:-1]

def create_notion_page(dbid, title="Notebook Title", description="Notebook Description"):
    URL = 'https://api.notion.com/v1/pages'
    skey = os.environ.get('NOTION_API_KEY')
    headers = {
        "Authorization": "Bearer " + skey,
        "Content-Type": "application/json",
        "Notion-Version": "2022-02-22"
    }
    data = {
        "parent": { "type": "database_id", "database_id":f"{dbid}"},
        "properties": {
            "title": {
                "title": [{"type": "text", "text": { "content": title}}]
            }
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": description}}]
                }
            }
        ],
    }

    result = requests.post(URL, headers=headers, json=data).json()
    print(result)
    return result['id'], result['url']

def create_fake_notion_page(title="Notebook Title"):
    url = 'http://localhost:8080/pages/'
    data = {"blocks": [{"tag": "h1", "html": title, "imageUrl": ""},{"tag": "p", "html": "", "imageUrl": ""}]}
    headers = {"Content-Type": "application/json"}
    res = requests.post(url, json=data, headers=headers)
    res = json.loads(res.text)
    return res['pageId']


class NotebookForm(forms.ModelForm):

    template_name = 'notes/notes_form_snippet.html'

    database_url = forms.URLField(required=True)

    class Meta:
        model = Notebook
        fields = ['title', 'description']

    def save(self, user, commit=True):
        notebook = super(NotebookForm, self).save(commit=False)
        dburl = self.cleaned_data['database_url']
        dbid = dbid_from_url(dburl)
        print("dbid:", dbid)
        nd = NotebookDatabase.objects.get_or_create(url=dburl, id=dbid, user=user)
        print(nd)
        notebook.notebook_id, notebook.url = create_notion_page(dbid, notebook.title, notebook.description)
        if commit:
            notebook.save()
        return notebook
