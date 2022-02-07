from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/export/', views.export_users, name='user_list'),
    path('profile/', views.UserUpdateView.as_view(), name='profile'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(), name='changepassword'),
]
