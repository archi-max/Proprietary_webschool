from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    # path('edit/<int:pk>', views.NotebookDetailView.as_view(), name='edit_notebook'),
    # path('edit/<int:pk>', views.notebook_view, name='edit_notebook'),
    # path('edit/<int:pk>/save', views.notebook_save_view, name='save_notebook'),
    path('', views.NotebookListView.as_view(), name='list'),
    path('new', views.NotebookFormView.as_view(), name='new'),
    path('<int:pk>/edit', views.NotebookUpdateView.as_view(), name='edit'),
]

