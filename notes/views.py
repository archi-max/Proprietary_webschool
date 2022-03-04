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

# def notebook_view(request, pk):
#     notebook = Notebook.objects.get(id=pk)
#     d = notebook.data
#     data = {
#         "blocks":d,
#         "notebook_id":pk
#     }
#     r = JsonResponse(data, safe=False)
#     r.headers['Access-Control-Allow-Origin'] = '*'
#     return r
#
# @csrf_exempt
# def notebook_save_view(request, pk):
#     notebook = Notebook.objects.get(id=pk)
#
#     if request.method == "POST":
#         notebook.data = json.loads(request.body)
#         notebook.save()
#         print(notebook.data)
#         r = JsonResponse({'status': 'ok'})
#     else:
#         r = JsonResponse({"error": f"{request.method} Method not allowed"}, status=405)
#         print(f"{request.method} Method not allowed")
#     r.headers['Access-Control-Allow-Origin'] = '*'
#     return r

# class NotebookDetailView(DetailView):
#     model = Notebook
#     template_name = 'notes/documents.html'
    
#     def dispatch(self, *args, **kwargs):
#         response = super(NotebookDetailView, self).dispatch(*args, **kwargs)
#         response["Access-Control-Allow-Origin"] = "*"
#         return response


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

class NotebookUpdateView(UpdateView):
    model = Notebook
    template_name = 'notes/form.html'
    fields = ['title', 'description']
    success_url = '/notes/'
