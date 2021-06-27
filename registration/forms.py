from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='имя')
    email = forms.CharField(label='электронная почта')
    password0 = forms.CharField(label='пароль', widget=forms.PasswordInput)
    password1 = forms.CharField(label='повторите пароль', widget=forms.PasswordInput)