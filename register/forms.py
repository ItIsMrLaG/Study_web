from django.contrib.auth.forms import UserCreationForm
from django import forms

# UserCreationForm - can be used for work with user-table inside db

class UserRegist_form(UserCreationForm):
    email = forms.EmailField(required=True)
    field_order = ['username', 'email', 'password1', 'password2']
