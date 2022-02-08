from django.urls import path
from . import views
app_name = 'homework'

urlpatterns = [
    path('', views.WorkListView.as_view(), name='work_list'),
    path('work/create/', views.WorkFormView.as_view(), name='work_create'),
    path('work/<int:pk>/edit/', views.WorkUpdateView.as_view(), name='work_update'),
    path('work/<int:pk>/delete/', views.WorkDeleteView.as_view(), name='work_delete'),
    path('submissions/<int:pk>/', views.SubmissionListView.as_view(), name='submission_list'),
    path('submissions/<int:pk>/create/', views.SubmissionFormView.as_view(), name='submission_create'),
    path('submissions/<int:pk>/edit/', views.SubmissionUpdateView.as_view(), name='submission_update')
]