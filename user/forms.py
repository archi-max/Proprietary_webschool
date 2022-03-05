# from django import forms
# from django.contrib.auth import get_user_model
# User = get_user_model()
#
# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']

from django import forms
from django.contrib.auth.models import Group


class NewGroupForm(forms.ModelForm):
    template_name = "user/forms/new_group_snippet.html"

    class Meta:
        model = Group
        fields = ("name",)
