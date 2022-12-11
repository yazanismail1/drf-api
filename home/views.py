from django.shortcuts import render
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'home_template_view.html'

class DocsTemplateView(TemplateView):
    template_name = 'docs_template_view.html'