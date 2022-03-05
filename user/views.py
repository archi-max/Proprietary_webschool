from django.contrib.auth import  get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import TemplateView, ListView
import csv
from django.contrib.auth import views as auth_views
from django.urls import reverse

### FORMS

from django import forms

# class UserCreationForm(forms.ModelForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'user_type')

### VIEWS

User = get_user_model()

def export_users(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="userlist.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['admission number', 'email', 'first_name', 'last_name'])
    for user in User.objects.filter(groups__in=request.user.groups.all()).distinct():
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
    success_url = '/formsuccess/'
    fields = ('first_name', 'last_name', 'email', 'password', 'user_type', 'avatar', 'groups')

    def form_invalid(self, form):
        f = self.get_form()
        return render(self.request, 'backend/form_error.html', {'form': f})

    def form_valid(self, form):
        user = form.save(commit=True)
        user.set_password(form.cleaned_data['password'])
        print(form.cleaned_data)
        for grp in form.cleaned_data['groups']: user.groups.add(grp)
        return super(UserCreateView, self).form_valid(form)

class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        res = User.objects.filter(groups__in=self.request.user.groups.all()).distinct()
        return res

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user/user_list.html'
    success_url = "/user/list/"