from django.urls import path
from .views import *


url_patterns = [
    path('home/', HomeView.as_view(), name='home-name')
]