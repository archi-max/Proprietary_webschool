from django.contrib.auth import  get_user_model
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
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
    success_url = '/'
    fields = '__all__'

    def get_object(self, queryset=None):
        return self.request.user


class UserLogoutView(auth_views.LogoutView):
    model = User
    success_url = "/login"