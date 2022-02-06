from django.urls import path

from . import views

app_name='posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='view'),
    path('myposts/', views.PostsCreatedViews.as_view(), name='myposts'),
    path('create/', views.PostFormView.as_view(), name='create'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
]