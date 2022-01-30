from django.shortcuts import render
from .models import Notebook
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests as r
from django.views.generic.edit import FormView
from .forms import NotebookForm
# Create your views here.

def notebook_view(request, pk):
    notebook = Notebook.objects.get(id=pk)
    d = notebook.data
    data = {
        "blocks":d,
        "notebook_id":pk
    }
    r = JsonResponse(data, safe=False)
    r.headers['Access-Control-Allow-Origin'] = '*'
    return r

@csrf_exempt
def notebook_save_view(request, pk):
    notebook = Notebook.objects.get(id=pk)

    if request.method == "POST":
        notebook.data = json.loads(request.body)
        notebook.save()
        print(notebook.data)
        r = JsonResponse({'status': 'ok'})
    else:
        r = JsonResponse({"error": f"{request.method} Method not allowed"}, status=405)
        print(f"{request.method} Method not allowed")
    r.headers['Access-Control-Allow-Origin'] = '*'
    return r

# class NotebookDetailView(DetailView):
#     model = Notebook
#     template_name = 'notes/notebook_detail.html'
#
#     def dispatch(self, *args, **kwargs):
#         response = super(NotebookDetailView, self).dispatch(*args, **kwargs)
#         response["Access-Control-Allow-Origin"] = "*"
#         return response


class NotebookFormView(FormView):
    template_name = 'notes/notebook_form.html'
    form_class = NotebookForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def dispatch(self, *args, **kwargs):
        response = super(NotebookFormView, self).dispatch(*args, **kwargs)
        response["Access-Control-Allow-Origin"] = "*"
        return response
