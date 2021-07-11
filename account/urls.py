from django.urls import include
from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration-name'),
    path('registration/done/', RegistrationDoneView.as_view(), name='registration_done-name'),
    path('login/', LoginView.as_view(), name='login-name'),
]