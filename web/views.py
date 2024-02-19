import json
from typing import Any
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import HttpRequest, JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

import authAPI
import courseAPI.models
import utilsAPI
from utilsAPI.models import Testimonial, Announcement
from .models import *
from authAPI.models import User
from orderAPI.models import UserPurchase

# Create your views here.

# @register.filter
# def get_range(value):
#     return range(value)

class BaseView(TemplateView):
    template_name = 'partials/base.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        fields = courseAPI.models.Field.objects.all()
        testimonials = Testimonial.objects.all()[:3]
        footer_navs = FooterNav.objects.all()
        announcements = Announcement.objects.all()
        static_pages = StaticPage.objects.all()
        specializations = courseAPI.models.Specialization.objects.all()
        hero_fields = fields[:5]

        data = {
            'testimonials': testimonials,
            'page': 'home',
            'fields': fields,
            'footer_navs': footer_navs,
            'static_pages': static_pages,
            'announcement': announcements.first(),
            'announcements': announcements,
            'hero_fields': hero_fields,
            'specializations': specializations,
        }

        context = data
        return context

class HomeView(BaseView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    

    def get(self, request, *args, **kwargs):
        carousels = CourseCarousel.objects.all()[:4]
        user_courses_carousels = None

        latest = courseAPI.models.Course.objects.all()[:8]
        latest_carousel = {
            'title': 'Latest',
            'courses': latest,
        }


        if request.user.is_authenticated:
            user_courses = courseAPI.models.UserCourse.objects.filter(user=request.user)
            user_courses_carousels = {
                'title': 'Enrolled Courses',  # request.user.get_full_name(),
                'courses': user_courses,
                'is_user_carousel': True,
            }

        # print(data['user_courses_carousels'])
        data = self.get_context_data()
        data['carousels'] = carousels
        data['latest_carousel'] = latest_carousel
        data['user_courses_carousels'] = user_courses_carousels

        context = {'data': data}
        return render(request, self.template_name, context)


class ProfileView(BaseView):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        data = self.get_context_data()
        context = data
        return render(request, self.template_name, context)


class LearnView(BaseView):
    template_name = 'learn.html'

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        course_data = courseAPI.models.Course.objects.get(id=kwargs['pk'])
        classes = courseAPI.models.Class.objects.filter(course=kwargs['pk']).order_by('class_number')
        notes = utilsAPI.models.Note.objects.filter(course=course_data).order_by('-date')
        announcements = utilsAPI.models.Announcement.objects.filter(course=course_data).order_by('-date')
        user_owns_course = UserPurchase.objects.filter(user=request.user, course=kwargs['pk']).exists()

        # print(user_owns_course)

        if course_data.skills is not None:
            course_data.skills = course_data.skills.split('.')
        if course_data.tags is not None:
            course_data.tags = course_data.tags.split(', ')
        if course_data.objectives is not None:
            course_data.objectives = course_data.objectives.split('.')

        for class_ in classes:
            if class_.objectives is not None:
                class_.objectives = class_.objectives.split('.')

        data = self.get_context_data()
        data['course_data'] = course_data
        data['classes'] = classes
        data['page'] = kwargs['page']
        data['notes'] = notes
        data['announcements'] = announcements
        data['user_owns_course'] = user_owns_course

        context = {'data': data}
        return render(request, self.template_name, context)


class DashboardView(BaseView):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        q = request.GET.get('q')
        fields = courseAPI.models.Field.objects.all()
        courses = courseAPI.models.UserCourse.objects.filter(user=request.user).all()

        data = self.get_context_data()
        data['q'] = q
        data['courses'] = courses
        data['page'] = 'explore'

        context = {'data': data}
        return render(request, self.template_name, context)


class CourseView(BaseView):
    template_name = 'course.html'

    def get(self, request, *args, **kwargs):
        course_data = courseAPI.models.Course.objects.get(id=kwargs['pk'])
        classes = courseAPI.models.Class.objects.filter(course=course_data)

        user_owns_course = None

        if request.user.is_authenticated:
            user_owns_course = courseAPI.models.UserCourse.objects.filter(user=request.user, course=kwargs['pk'])


        if course_data.skills is not None:
            course_data.skills = course_data.skills.split('.') or course_data.skills.split(', ') 
        if course_data.tags is not None:
            course_data.tags = course_data.tags.split(', ')
        if course_data.objectives is not None:
            course_data.objectives = course_data.objectives.split('.')

        data = self.get_context_data()
        data['course_data'] = course_data
        data['classes'] = classes
        data['page'] = 'course'
        data['user_owns_course'] = user_owns_course

        context = {'data': data}
        return render(request, self.template_name, context)


class ExploreView(BaseView):
    template_name = 'explore.html'

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')

        if q is not None:
            courses = courseAPI.models.Course.objects.filter(title__icontains=q)
        else:
            courses = courseAPI.models.Course.objects.all()

        data = self.get_context_data()
        data['courses'] = courses
        data['page'] = 'explore'
        data['q'] = q

        context = {'data': data}
        return render(request, self.template_name, context)


class EnrollView(BaseView):
    template_name = 'enroll.html'

    def get(self, request, *args, **kwargs):
        course_data = courseAPI.models.Course.objects.get(id=kwargs['pk'])

        data = self.get_context_data()
        data['course_data'] = course_data
        data['page'] = 'enroll'

        context = {'data': data}
        return render(request, self.template_name, context)


class StaticPageView(BaseView):
    template_name = 'static.html'

    def get(self, request, *args, **kwargs):
        page = kwargs['page']
        static_pages = StaticPage.objects.all()

        for static_page in static_pages:
            static_page.content = static_page.content.split('\n')

        data = self.get_context_data()
        data['page'] = page
        data['static_pages'] = static_pages

        context = {'data': data}
        return render(request, self.template_name, context)


class LoginView(BaseView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):

        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            return redirect('home')

        data = self.get_context_data()
        data['page'] = 'login'

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


class SignUpView(BaseView):
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):

        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            return redirect('home')

        data = self.get_context_data()
        data['page'] = 'signup'

        context = {'data': data}
        return render(request, self.template_name, context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')
