import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

import authAPI
import courseAPI.models
import utilsAPI
from utilsAPI.models import Testimonial, Announcement
from .models import *

# Create your views here.

# @register.filter
# def get_range(value):
#     return range(value)


class LearnView(TemplateView):
    template_name = 'learn.html'

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        course_data = courseAPI.models.Course.objects.get(id=kwargs['pk'])
        classes = courseAPI.models.Class.objects.filter(course=kwargs['pk']).order_by('class_number')
        notes = utilsAPI.models.Note.objects.filter(course=course_data).order_by('-date')
        announcements = utilsAPI.models.Announcement.objects.filter(course=course_data).order_by('-date')

        if course_data.skills is not None:
            course_data.skills = course_data.skills.split(', ')
        if course_data.tags is not None:
            course_data.tags = course_data.tags.split(', ')
        if course_data.objectives is not None:
            course_data.objectives = course_data.objectives.split('.')

        for class_ in classes:
            if class_.objectives is not None:
                class_.objectives = class_.objectives.split('.')

        data = {
            'course_data': course_data,
            'classes': classes,
            'page': kwargs['page'],
            'notes': notes,
            'announcements': announcements,
        }
        context = {'data': data}
        return render(request, self.template_name, context)


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        footer_navs = FooterTitle.objects.all()

        q = request.GET.get('q')
        fields = courseAPI.models.Field.objects.all()
        courses = courseAPI.models.UserCourse.objects.filter(user=request.user).all()

        # print(courses)
        data = {
            'q': q,
            'courses': courses,
            'footer_navs': footer_navs,
            'page': 'explore',
        }
        context = {'data': data}
        return render(request, self.template_name, context)


class CourseView(TemplateView):
    template_name = 'course.html'

    def get(self, request, *args, **kwargs):
        course_data = courseAPI.models.Course.objects.get(id=kwargs['pk'])
        testimonials = Testimonial.objects.all()[:3]
        classes = courseAPI.models.Class.objects.filter(course=course_data)
        topnavs = BusinessModel.objects.all()


        if course_data.skills is not None:
            course_data.skills = course_data.skills.split(', ')
        if course_data.tags is not None:
            course_data.tags = course_data.tags.split(', ')
        if course_data.objectives is not None:
            course_data.objectives = course_data.objectives.split('.')

        footer_navs = FooterTitle.objects.all()

        # print(course_data)
        data = {
            'course_data': course_data,
            'testimonials': testimonials,
            'page': 'course',
            'classes': classes,
            'footer_navs': footer_navs,
            'topnavs': topnavs,
        }
        # print(data)
        context = {'data': data}
        return render(request, self.template_name, context)


class ExploreView(TemplateView):
    template_name = 'explore.html'

    def get(self, request, *args, **kwargs):
        footer_navs = FooterTitle.objects.all()
        topnavs = BusinessModel.objects.all()


        q = request.GET.get('q')

        if q is not None:
            courses = courseAPI.models.Course.objects.filter(field__title__icontains=q)
        else:
            courses = courseAPI.models.Course.objects.all()

        fields = courseAPI.models.Field.objects.all()

        # print(courses)
        data = {
            'q': q,
            'courses': courses,
            'fields': fields,
            'footer_navs': footer_navs,
            'page': 'explore',
            'topnavs': topnavs,
        }
        context = {'data': data}
        return render(request, self.template_name, context)


class EnrollView(TemplateView):
    template_name = 'enroll.html'

    def get(self, request, *args, **kwargs):
        footer_navs = FooterTitle.objects.all()
        course_data = courseAPI.models.Course.objects.get(id=kwargs['pk'])
        topnavs = BusinessModel.objects.all()

        # print(course_data)
        data = {
            'course_data': course_data,
            'page': 'enroll',
            'footer_navs': footer_navs,
            'topnavs': topnavs,
        }
        # print(data)
        context = {'data': data}
        return render(request, self.template_name, context)


class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        fields = courseAPI.models.Field.objects.all()[:15]
        testimonials = Testimonial.objects.all()[:3]
        carousels = CourseCarousel.objects.all()[:4]
        footer_navs = FooterTitle.objects.all()
        announcement = Announcement.objects.all().first()
        topnavs = BusinessModel.objects.all()

        user_courses_carousels = None

        if request.user.is_authenticated:
            user_courses = courseAPI.models.UserCourse.objects.filter(user=request.user)
            user_courses_carousels = {
                'title': 'Enrolled Courses',  # request.user.get_full_name(),
                'courses': user_courses,
                'is_user_carousel': True,
            }

        data = {
            'carousels': carousels,
            'testimonials': testimonials,
            'page': 'home',
            'fields': fields,
            'footer_navs': footer_navs,
            'topnavs': topnavs,
            'user_courses_carousels': user_courses_carousels,
            'announcement': announcement,
        }

        # print(data['user_courses_carousels'])
        context = {'data': data}
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get(self, request, *args, **kwargs):
        footer_navs = FooterTitle.objects.all()
        topnavs = BusinessModel.objects.all()

        data = {
            'footer_navs': footer_navs,
            'topnavs': topnavs,
        }
        context = {'data': data}
        return render(request, self.template_name, context)


class PrivacyView(TemplateView):
    template_name = 'pages/privacy.html'

    def get(self, request, *args, **kwargs):
        footer_navs = FooterTitle.objects.all()
        topnavs = BusinessModel.objects.all()

        data = {
            'footer_navs': footer_navs,
            'topnavs': topnavs,
        }
        context = {'data': data}
        return render(request, self.template_name, context)


class ContactView(TemplateView):
    template_name = 'pages/contact.html'

    def get(self, request, *args, **kwargs):
        footer_navs = FooterTitle.objects.all()
        topnavs = BusinessModel.objects.all()

        data = {
            'footer_navs': footer_navs,
            'topnavs': topnavs,
        }
        context = {'data': data}
        return render(request, self.template_name, context)


class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):

        footer_navs = FooterTitle.objects.all()

        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            return redirect('home')

        data = {
            'page': 'login',
            'footer_navs': footer_navs,
        }
        context = {'data': data}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        print(data)

        email = data.get('email')
        password = data.get('password')
        print(email)

        user = authenticate(email=email, password=password)

        if user and not user.is_superuser:
            login(request, user)
            return redirect('home')
        else:
            return JsonResponse({'success': False, 'error': 'Invalid login credentials'})


class SignUpView(TemplateView):
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        footer_navs = FooterTitle.objects.all()

        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            return redirect('home')

        data = {
            'page': 'signup',
            'footer_navs': footer_navs,
        }
        context = {'data': data}
        return render(request, self.template_name, context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')
