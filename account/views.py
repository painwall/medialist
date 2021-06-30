from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import View
from .forms import UserRegistrationForm
from .exceptions import RegistrationError


class RegistrationView(View):
    template_name = 'registration.html'
    def get(self, request, error=None):
        registration_form = UserRegistrationForm()
        return render(request, RegistrationView.template_name, {'registration_form': registration_form, 'error': error})

    def post(self, request):
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            result = self.create_user(registration_form.cleaned_data)
            if result['result']:
                return redirect('registration_done')
            else:
                return render(request, RegistrationView.template_name, {'registration_form': registration_form, 'error': result['data']})

    def create_user(self, data):

        try:
            new_user = User()
            all_users = User.objects.all().filter(username=data['username'], email=data['email'])

            if any(user.username == data['username'] for user in all_users):
                raise RegistrationError(f'Пользователь с таким именем ({data["username"]} уже существует)')

            if any(user.email == data['email'] for user in all_users):
                raise RegistrationError(f'Пользователь с такой почтой ({data["email"]}) уже существует')


            if data['password0'] != data['password1']:
                raise RegistrationError(f'Введенные пароли разные')

            new_user.username = data['username']
            new_user.email = data['email']
            new_user.set_password(data['password0'])
            new_user.save()



        except RegistrationError as error:
            return {'result': False, 'data': error.message}



        return {'result': True, 'data': data}

class RegistrationDoneView(View):
    template_name = 'registration_done.html'
    def get(self, request):
        return render(request, RegistrationDoneView.template_name)