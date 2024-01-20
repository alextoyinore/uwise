from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = 'pages/about.html'


class PrivacyView(TemplateView):
    template_name = 'pages/privacy.html'


class ContactView(TemplateView):
    template_name = 'pages/contact.html'


class AuthView(TemplateView):
    template_name = 'pages/auth.html'


class PageView(TemplateView):
    template_name = 'pages/page.html'

    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', '')
        context = {'page': page}
        return render(request, self.template_name, context)
