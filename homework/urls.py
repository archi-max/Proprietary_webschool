from django.urls import path
from . import views
app_name = 'homework'

urlpatterns = [
    path('', views.WorkListView.as_view(), name='work_list'),
    path('work/create/', views.WorkCreateView.as_view(), name='work_create'),
    path('work/<int:pk>/edit/', views.WorkUpdateView.as_view(), name='work_update'),
    path('submissions/<int:pk>/', views.SubmissionListView.as_view(), name='submission_list'),
    path('submissions/<int:pk>/create/', views.SubmissionCreateView.as_view(), name='submission_create'),
    path('submissions/<int:pk>/edit/', views.SubmissionUpdateView.as_view(), name='submission_update')
]