from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

    dummy_data = {
        'carousels': [
            {
                'id': 1,
                'title': 'Programming & Software',
                'courses': [
                    {
                        'id': 1,
                        'image': 'https://cdn.pixabay.com/photo/2021/08/04/13/06/software-developer-6521720_640.jpg',
                        'title': 'Python for Automation and Machine Learning',
                        'duration': 28,
                        'level': 'Intermediate'
                    },
                    {
                        'id': 2,
                        'image': 'https://images.pexels.com/photos/424436/pexels-photo-424436.jpeg?auto=compress&cs=tinysrgb&w=600',
                        'title': 'JavaScript for Everyone',
                        'duration': 28,
                        'level': 'Beginner'
                    },
                    {
                        'id': 3,
                        'image': 'https://images.pexels.com/photos/256381/pexels-photo-256381.jpeg?auto=compress&cs=tinysrgb&w=600',
                        'title': 'Introduction to Databases',
                        'duration': 28,
                        'level': 'Beginner'
                    },
                    {
                        'id': 4,
                        'image': 'https://images.pexels.com/photos/1105379/pexels-photo-1105379.jpeg?auto=compress&cs=tinysrgb&w=600',
                        'title': 'Django Web Development',
                        'duration': 28,
                        'level': 'Beginner'
                    },
                    {
                        'id': 5,
                        'image': 'https://images.pexels.com/photos/336232/pexels-photo-336232.jpeg?auto=compress&cs=tinysrgb&w=600',
                        'title': 'Django Rest Framework for API Development',
                        'duration': 28,
                        'level': 'Beginner'
                    },
                    {
                        'id': 6,
                        'image': 'https://images.pexels.com/photos/943096/pexels-photo-943096.jpeg?auto=compress&cs=tinysrgb&w=600',
                        'title': 'Git and Github for Version Control',
                        'duration': 28,
                        'level': 'Intermediate'
                    },
                    {
                        'id': 7,
                        'image': 'https://images.pexels.com/photos/785418/pexels-photo-785418.jpeg?auto=compress&cs=tinysrgb&w=600',
                        'title': 'Advanced Backend Development Topics',
                        'duration': 28,
                        'level': 'Advanced'
                    },
                    {
                        'id': 8,
                        'image': 'https://images.pexels.com/photos/404280/pexels-photo-404280.jpeg?auto=compress&cs=tinysrgb&w=600',
                        'title': 'Capstone Backend Development',
                        'duration': 28,
                        'level': 'Advanced'
                    },
                    {
                        'id': 9,
                        'image': 'https://images.pexels.com/photos/2653362/pexels-photo-2653362.jpeg?auto=compress&cs=tinysrgb&w=600',
                        'title': 'Build something with your new skill',
                        'duration': 28,
                        'level': 'Intermediate'
                    },
                    {
                        'id': 4,
                        'image': 'https://images.pexels.com/photos/256302/pexels-photo-256302.jpeg?auto=compress&cs=tinysrgb&w=600',
                        'title': 'Interview Preparation',
                        'duration': 14,
                        'level': 'Advanced'
                    }
                ]
            }
        ]
       
    }

    def get(self, request, *args, **kwargs):
        context = {'carousel_data': self.dummy_data}
        return render(request, self.template_name, context)

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
