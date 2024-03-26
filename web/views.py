import json
from typing import Any
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import Http404, HttpRequest, JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

import authAPI
import blogAPI
import courseAPI.models
import utilsAPI
from utilsAPI.models import Testimonial, Announcement
from .models import *
from authAPI.models import User
from orderAPI.models import UserPurchase

# Create your views here.

class BaseView(TemplateView):
    template_name = 'partials/base.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        fields = courseAPI.models.Field.objects.filter(is_active=True).all()
        testimonials = Testimonial.objects.all()[:5]
        footer_navs = FooterNav.objects.filter(is_active=True).all()
        announcements = Announcement.objects.all()
        static_pages = StaticPage.objects.filter(is_active=True).all()
        specializations = courseAPI.models.Course.objects.filter(is_specialization=True).all()
        blogs = blogAPI.models.Post.objects.filter(is_published=True).all().order_by('-date_posted')

        data = {
            'testimonials': testimonials,
            'page': 'home',
            'fields': fields,
            'footer_navs': footer_navs,
            'static_pages': static_pages,
            'announcement': announcements.first(),
            'announcements': announcements,
            'specializations': specializations,
            'blogs': blogs,
        }

        context = data
        return context

class HomeView(BaseView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    

    def get(self, request, *args, **kwargs):
        carousels = CourseCarousel.objects.filter(is_active=True).all().order_by('date')[:5]
        user_courses_carousels = None

        latest = courseAPI.models.Course.objects.all()[:10]
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
        specialization_carousel = {
            'title': 'Specializations',
            'courses': data['specializations']
        }

        data['carousels'] = carousels
        data['latest'] = latest
        data['user_courses_carousels'] = user_courses_carousels
        data['specialization_carousel'] = specialization_carousel

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
        course_data.description = course_data.description.split('\n')
        classes = courseAPI.models.Class.objects.filter(course=kwargs['pk']).order_by('class_number')
        notes = utilsAPI.models.Note.objects.filter(course=course_data).order_by('-date')
        announcements = utilsAPI.models.Announcement.objects.filter(course=course_data).order_by('-date')
        user_owns_course = UserPurchase.objects.filter(user=request.user, course=kwargs['pk']).exists()
        review = utilsAPI.models.Review.objects.filter(user=request.user, course=course_data).first()
        course_grades = utilsAPI.models.Grade.objects.filter(user=request.user, course=course_data)

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
        data['course_grades'] = course_grades

        if review is not None:
            data['review'] = review

        context = {'data': data}
        return render(request, self.template_name, context)


class DashboardView(BaseView):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        q = request.GET.get('q')
        fields = courseAPI.models.Field.objects.all()
        courses = courseAPI.models.UserCourse.objects.filter(user=request.user).all().order_by('-date')
        purchased_courses = UserPurchase.objects.filter(user=request.user).all()
        favourites = utilsAPI.models.Favourite.objects.filter(user=request.user).all()

        data = self.get_context_data()
        data['q'] = q
        data['courses'] = courses
        data['purchased_courses'] = purchased_courses
        data['favourites'] = favourites
        data['page'] = 'explore'

        context = {'data': data}
        return render(request, self.template_name, context)


class CourseView(BaseView):
    template_name = 'course.html'

    def get(self, request, *args, **kwargs):
        try:
            course_data = courseAPI.models.Course.objects.get(id=kwargs['pk'])
        except Course.DoesNotExist:
            raise Http404("Course does not exist")
        
        classes = courseAPI.models.Class.objects.filter(course=course_data)

        specialization_courses = courseAPI.models.SpecializationCourse.objects.filter(specialization=course_data)

        specialization_courses_carousel = {
            'title': 'Courses in this specialization',
            'courses': specialization_courses,
        }

        print(specialization_courses)

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
        data['specialization_courses_carousel'] = specialization_courses_carousel
        data['specialization_courses'] = specialization_courses

        context = {'data': data}
        return render(request, self.template_name, context)


class ExploreView(BaseView):
    template_name = 'explore.html'

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')

        if q is not None:
            courses = courseAPI.models.Course.objects.filter(title__icontains=q, is_active=True)
        else:
            courses = courseAPI.models.Course.objects.filter(is_active=True).all()

        data = self.get_context_data()
        data['courses'] = courses
        data['page'] = 'explore'
        data['q'] = q

        context = {'data': data}
        return render(request, self.template_name, context)
    

class BlogsView(BaseView):
    template_name = 'blogs.html'

    def get(self, request, *args, **kwargs):
        featured = blogAPI.models.Post.objects.filter(featured=True, is_published=True).first()
        data = self.get_context_data()
        data['featured'] = featured
        context = {'data': data}
        return render(request, self.template_name, context)


class BlogView(BaseView):
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        try:
            blog = blogAPI.models.Post.objects.get(id=kwargs['pk'])
        except blogAPI.models.Post.DoesNotExist:
            raise Http404("Course does not exist")
        
        blog.content = blog.content.split('\n')
        
        data = self.get_context_data()
        data['blog'] = blog
        data['prev']=blog.id-1
        data['next']=blog.id+1
        context = {'data': data}
        return render(request, self.template_name, context)

class EnrollView(BaseView):
    template_name = 'enroll.html'

    def get(self, request, *args, **kwargs):
        try:
            course_data = courseAPI.models.Course.objects.get(id=kwargs['pk'])
        except Course.DoesNotExist:
            raise Http404("Course does not exist")

        data = self.get_context_data()
        data['course_data'] = course_data
        data['page'] = 'enroll'

        context = {'data': data}
        return render(request, self.template_name, context)


class StaticPageView(BaseView):
    template_name = 'static.html'

    def get(self, request, *args, **kwargs):
        page = kwargs['page']
        static_pages = StaticPage.objects.filter(is_active=True).all()

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

def handle404(request):
    return render(request, template_name='404.html', status=404)
