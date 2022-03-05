from django.shortcuts import render
from .models import Notebook
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.generic.detail import DetailView
import requests as r
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import ListView
from .forms import NotebookForm
# Create your views here.


class NotebookFormView(FormView):
    template_name = 'backend/form_page.html'
    form_class = NotebookForm
    success_url = '/formsuccess/'

    def form_valid(self, form):
        notebook = form.save(user=self.request.user,commit=False)
        notebook.created_by = self.request.user
        notebook.save()
        return super().form_valid(form)

class NotebookListView(ListView):
    model = Notebook
    template_name = 'notes/list.html'

    def get_queryset(self):
        return Notebook.objects.filter(created_by=self.request.user).order_by('-created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.request.user.notebookdatabase_set.all().order_by('-created_at')
        print("q",q)
        if len(q) > 0:
            print("using existing vals:")
            form = NotebookForm(initial={'database_url': q[0].url})
        else:
            form = NotebookForm()
        context['notebook_create_form'] = form
        return context