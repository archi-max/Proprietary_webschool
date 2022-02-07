from django.contrib.auth import  get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView
import csv
from django.contrib.auth import views as auth_views
from django.urls import reverse

User = get_user_model()

def export_users(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="userlist.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['admission number', 'email', 'first_name', 'last_name'])
    for user in User.objects.all():
        writer.writerow([user.user_id, user.email, user.first_name, user.last_name])

    return response


class UserUpdateView(UpdateView):
    model = User
    template_name = 'user/profile.html'
    success_url = '/profile/'
    fields = ('avatar', 'first_name', 'last_name', 'email')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        print("form validating")
        print(form.files)
        return super().form_valid(form)

def custom_update_view(request):
    if request.method == 'POST':
        pass

    return render(request, 'user/profile.html', {'user': request.user})

class UserLogoutView(auth_views.LogoutView):
    model = User
    success_url = "/login"


class UserCreateView(CreateView):
    model = User
    template_name = 'user/user_add.html'
    success_url = '#'
    fields = ( 'first_name', 'last_name', 'email', 'password', 'user_type', 'avatar')

    def form_valid(self, form):
        print("form validating")
        print(form.field['password1'])
        return super().form_valid(form)