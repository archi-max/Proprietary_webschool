from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/form.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
]
