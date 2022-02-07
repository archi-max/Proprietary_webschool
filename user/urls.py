from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', views.UserLogoutView.as_view(next_page="/login"), name='logout'),
    path('users/export/', views.export_users, name='user_list'),
    path('profile/', views.UserUpdateView.as_view(), name='profile'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name="backend/form_error.html", success_url="/formsuccess/"), name='changepassword'),
    path('user/add/', views.UserCreateView.as_view(), name='user_add'),
]
