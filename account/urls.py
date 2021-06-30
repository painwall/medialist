from django.urls import include
from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('registration/done/', RegistrationDoneView.as_view(), name='registration_done'),
]