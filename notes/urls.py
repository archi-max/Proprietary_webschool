from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    # path('edit/<int:pk>', views.NotebookDetailView.as_view(), name='edit_notebook'),
    path('edit/<int:pk>', views.notebook_view, name='edit_notebook'),
    path('edit/<int:pk>/save', views.notebook_save_view, name='save_notebook'),
]