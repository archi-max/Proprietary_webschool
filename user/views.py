from django.contrib.auth import  get_user_model
from django.http import HttpResponse
import csv

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
