from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = 'homepage.html'

    def get(self, request):
        return render(request, HomeView.template_name)