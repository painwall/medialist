from django.urls import include
from django.urls import path
from .views import *

urlpatterns = [
    path('', RegistrationView.as_view(), name='registration'),
    path('done', RegistrationDoneView.as_view(), name='registration_done'),
]