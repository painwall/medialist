from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='имя')
    email = forms.CharField(label='электронная почта')
    password0 = forms.CharField(label='пароль', widget=forms.PasswordInput)
    password1 = forms.CharField(label='повторите пароль', widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username_or_email = forms.CharField(label='имя или почта')
    password = forms.CharField(label='пароль', widget=forms.PasswordInput)