from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class testPage(TemplateView):
    template_name = 'index.html'