from django.urls import path
from . import views

app_name = 'classes'

urlpatterns = [
    path('create/', views.ClassCreateView.as_view(), name='create'),
    path('<int:pk>/update', views.ClassUpdateView.as_view(), name='update'),
    path('', views.ClassListView.as_view(), name='list'),
    path('day/<int:day>/', views.DayClassListView.as_view(), name='daylist'),
    path('join/<int:pk>/', views.ClassJoinView.as_view(), name='join'),
]