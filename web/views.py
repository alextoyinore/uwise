import json
from datetime import datetime

from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

import courseAPI.models
from utilsAPI.models import Testimonial
from .models import *

# Create your views here.

# @register.filter
# def get_range(value):
#     return range(value)


dummy_data = {
    'testimonials': [
        {
            'id': 1,
            'title': 'From our Alumni',
            'messages': [
                {
                    'id': 1,
                    'student_name': 'Kayode Olawale',
                    'student_photo': 'https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'message': 'At a time in my life when I needed a new direction, I found Uwise and it\'s been a blessing',
                    'date': '2020-05-21',
                },
                {
                    'id': 2,
                    'student_name': 'Olufade Blessing',
                    'student_photo': 'https://images.pexels.com/photos/2080383/pexels-photo-2080383.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'message': 'After Uwise, I launched my own startup as we are encouraged to do in the "What will you Build?" sessions.',
                    'date': '2023-08-21',
                },
                {
                    'id': 3,
                    'student_name': 'Toyin Abrahams',
                    'student_photo': 'https://images.pexels.com/photos/274610/pexels-photo-274610.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'message': 'After Uwise, I launched my own startup as we are encouraged to do in the "What will you Build?" sessions.',
                    'date': '2023-08-21',
                }
            ]
        }
    ],
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
                    'level': 'Intermediate',
                    'rating': 3,
                    'rating_count': 439
                },
                {
                    'id': 2,
                    'image': 'https://images.pexels.com/photos/424436/pexels-photo-424436.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'JavaScript for Everyone',
                    'duration': 28,
                    'level': 'Beginner',
                    'rating': 4,
                    'rating_count': 1035
                },
                {
                    'id': 3,
                    'image': 'https://images.pexels.com/photos/256381/pexels-photo-256381.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Introduction to Databases',
                    'duration': 28,
                    'level': 'Beginner',
                    'rating': 4,
                    'rating_count': 126
                },
                {
                    'id': 4,
                    'image': 'https://images.pexels.com/photos/1105379/pexels-photo-1105379.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Django Web Development',
                    'duration': 28,
                    'level': 'Beginner',
                    'rating': 5,
                    'rating_count': 435
                },
                {
                    'id': 5,
                    'image': 'https://images.pexels.com/photos/336232/pexels-photo-336232.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Django Rest Framework for API Development',
                    'duration': 28,
                    'level': 'Beginner',
                    'rating': 5,
                    'rating_count': 2045
                },
                {
                    'id': 6,
                    'image': 'https://images.pexels.com/photos/943096/pexels-photo-943096.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Git and Github for Version Control',
                    'duration': 28,
                    'level': 'Intermediate',
                    'rating': 4,
                    'rating_count': 516
                },
                {
                    'id': 7,
                    'image': 'https://images.pexels.com/photos/785418/pexels-photo-785418.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Advanced Backend Development Topics',
                    'duration': 28,
                    'level': 'Advanced',
                    'rating': 3,
                    'rating_count': 989
                },
                {
                    'id': 8,
                    'image': 'https://images.pexels.com/photos/404280/pexels-photo-404280.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Capstone Backend Development',
                    'duration': 28,
                    'level': 'Advanced',
                    'rating': 3,
                    'rating_count': 493
                },
                {
                    'id': 9,
                    'image': 'https://images.pexels.com/photos/2653362/pexels-photo-2653362.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Build something with your new skill',
                    'duration': 28,
                    'level': 'Intermediate',
                    'rating': 3,
                    'rating_count': 235
                },
                {
                    'id': 10,
                    'image': 'https://images.pexels.com/photos/256302/pexels-photo-256302.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Interview Preparation',
                    'duration': 14,
                    'level': 'Advanced',
                    'rating': 4,
                    'rating_count': 2674
                }
            ]
        },

        {
            'id': 2,
            'title': 'Vocational Trainings',
            'courses': [
                {
                    'id': 11,
                    'image': 'https://images.pexels.com/photos/336372/pexels-photo-336372.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Intro to Fashion Design',
                    'duration': 100,
                    'level': 'Beginner',
                    'rating': 4,
                    'rating_count': 439,
                },
                {
                    'id': 12,
                    'image': 'https://images.pexels.com/photos/1598505/pexels-photo-1598505.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Fundamentals of Shoe Making',
                    'duration': 100,
                    'level': 'Beginner',
                    'rating': 4,
                    'rating_count': 504
                },
                {
                    'id': 13,
                    'image': 'https://images.pexels.com/photos/973401/pexels-photo-973401.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Hair and Cosmetics',
                    'duration': 180,
                    'level': 'Beginner',
                    'rating': 4,
                    'rating_count': 783
                },
                {
                    'id': 14,
                    'image': 'https://images.pexels.com/photos/1249611/pexels-photo-1249611.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Carpentry and Wood Works',
                    'duration': 360,
                    'level': 'Beginner',
                    'rating': 5,
                    'rating_count': 402
                },
                {
                    'id': 15,
                    'image': 'https://images.pexels.com/photos/1492232/pexels-photo-1492232.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Aluminium works for Everybody',
                    'duration': 180,
                    'level': 'Beginner',
                    'rating': 5,
                    'rating_count': 902
                },
                {
                    'id': 16,
                    'image': 'https://images.pexels.com/photos/5532719/pexels-photo-5532719.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Laptop and Phone Engineering for Everybody',
                    'duration': 180,
                    'level': 'Intermediate',
                    'rating': 4,
                    'rating_count': 454
                },
                {
                    'id': 17,
                    'image': 'https://images.pexels.com/photos/65623/vehicle-chrome-technology-automobile-65623.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Mechanical Works and Auto Repairs',
                    'duration': 360,
                    'level': 'Advanced',
                    'rating': 3,
                    'rating_count': 1009
                },
                {
                    'id': 18,
                    'image': 'https://images.pexels.com/photos/404280/pexels-photo-404280.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Iron smelting and Welding',
                    'duration': 360,
                    'level': 'Advanced',
                    'rating': 3,
                    'rating_count': 420
                },
                {
                    'id': 19,
                    'image': 'https://images.pexels.com/photos/1474993/pexels-photo-1474993.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Visual Arts and Figure Painting',
                    'duration': 360,
                    'level': 'Intermediate',
                    'rating': 3,
                    'rating_count': 430
                },
                {
                    'id': 20,
                    'image': 'https://images.pexels.com/photos/1509534/pexels-photo-1509534.jpeg?auto=compress&cs=tinysrgb&w=600',
                    'title': 'Creative Arts and Metal Works',
                    'duration': 360,
                    'level': 'Advanced',
                    'rating': 4,
                    'rating_count': 3006
                }
            ]
        }
    ],

    'courses': [
        {
            'id': 1,
            'image': 'https://cdn.pixabay.com/photo/2021/08/04/13/06/software-developer-6521720_640.jpg',
            'title': 'Python for Automation and Machine Learning',
            'duration': 28,
            'level': 'Intermediate',
            'rating': 3,
            'rating_count': 439,
            'price': 200000,
            'next_start_date': datetime.today(),
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 2,
            'image': 'https://images.pexels.com/photos/424436/pexels-photo-424436.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'JavaScript for Everyone',
            'duration': 28,
            'level': 'Beginner',
            'rating': 4,
            'rating_count': 1035,
            'price': 200000,
            'next_start_date': datetime.today(),
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12',
                    'image': 'https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg?auto=compress&cs=tinysrgb&w=600'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13',
                    'image': 'https://images.pexels.com/photos/2080383/pexels-photo-2080383.jpeg?auto=compress&cs=tinysrgb&w=600'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 3,
            'image': 'https://images.pexels.com/photos/256381/pexels-photo-256381.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Introduction to Databases',
            'duration': 28,
            'level': 'Beginner',
            'rating': 4,
            'rating_count': 126,
            'price': 200000,
            'next_start_date': datetime.today(),
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 4,
            'image': 'https://images.pexels.com/photos/1105379/pexels-photo-1105379.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Django Web Development',
            'duration': 28,
            'level': 'Beginner',
            'rating': 5,
            'rating_count': 435,
            'price': 200000,
            'next_start_date': datetime.today(),
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 5,
            'image': 'https://images.pexels.com/photos/336232/pexels-photo-336232.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Django Rest Framework for API Development',
            'duration': 28,
            'level': 'Beginner',
            'rating': 5,
            'rating_count': 2045,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 6,
            'image': 'https://images.pexels.com/photos/943096/pexels-photo-943096.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Git and Github for Version Control',
            'duration': 28,
            'level': 'Intermediate',
            'rating': 4,
            'rating_count': 516,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 7,
            'image': 'https://images.pexels.com/photos/785418/pexels-photo-785418.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Advanced Backend Development Topics',
            'duration': 28,
            'level': 'Advanced',
            'rating': 3,
            'rating_count': 989,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 8,
            'image': 'https://images.pexels.com/photos/404280/pexels-photo-404280.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Capstone Backend Development',
            'duration': 28,
            'level': 'Advanced',
            'rating': 3,
            'rating_count': 493,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 9,
            'image': 'https://images.pexels.com/photos/2653362/pexels-photo-2653362.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Build something with your new skill',
            'duration': 28,
            'level': 'Intermediate',
            'rating': 3,
            'rating_count': 235,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 10,
            'image': 'https://images.pexels.com/photos/256302/pexels-photo-256302.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Interview Preparation',
            'duration': 14,
            'level': 'Advanced',
            'rating': 4,
            'rating_count': 2674,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 11,
            'image': 'https://images.pexels.com/photos/336372/pexels-photo-336372.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Intro to Fashion Design',
            'duration': 100,
            'level': 'Beginner',
            'rating': 4,
            'rating_count': 439,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 12,
            'image': 'https://images.pexels.com/photos/1598505/pexels-photo-1598505.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Fundamentals of Shoe Making',
            'duration': 100,
            'level': 'Beginner',
            'rating': 4,
            'rating_count': 504,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 13,
            'image': 'https://images.pexels.com/photos/973401/pexels-photo-973401.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Hair and Cosmetics',
            'duration': 180,
            'level': 'Beginner',
            'rating': 4,
            'rating_count': 783,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 14,
            'image': 'https://images.pexels.com/photos/1249611/pexels-photo-1249611.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Carpentry and Wood Works',
            'duration': 360,
            'level': 'Beginner',
            'rating': 5,
            'rating_count': 402,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 15,
            'image': 'https://images.pexels.com/photos/1492232/pexels-photo-1492232.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Aluminium works for Everybody',
            'duration': 180,
            'level': 'Beginner',
            'rating': 5,
            'rating_count': 902,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 16,
            'image': 'https://images.pexels.com/photos/5532719/pexels-photo-5532719.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Laptop and Phone Engineering for Everybody',
            'duration': 180,
            'level': 'Intermediate',
            'rating': 4,
            'rating_count': 454,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 17,
            'image': 'https://images.pexels.com/photos/65623/vehicle-chrome-technology-automobile-65623.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Mechanical Works and Auto Repairs',
            'duration': 360,
            'level': 'Advanced',
            'rating': 3,
            'rating_count': 1009,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 18,
            'image': 'https://images.pexels.com/photos/404280/pexels-photo-404280.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Iron smelting and Welding',
            'duration': 360,
            'level': 'Advanced',
            'rating': 3,
            'rating_count': 420,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 19,
            'image': 'https://images.pexels.com/photos/1474993/pexels-photo-1474993.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Visual Arts and Figure Painting',
            'duration': 360,
            'level': 'Intermediate',
            'rating': 3,
            'rating_count': 430,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        },
        {
            'id': 20,
            'image': 'https://images.pexels.com/photos/1509534/pexels-photo-1509534.jpeg?auto=compress&cs=tinysrgb&w=600',
            'title': 'Creative Arts and Metal Works',
            'duration': 360,
            'level': 'Advanced',
            'rating': 4,
            'rating_count': 3006,
            'price': 200000,
            'excerpt': 'This course introduces you to web development with the JavaScript '
                       'programming language using the React framework. The React framework '
                       'is one of the most popularly adopted framework among JavaScript developers '
                       'in the world of coding. React was given to the world by Meta (Facebook) in '
                       '2013 and has since grown to become the most adopted JavaScript framework beating '
                       'the likes of Angular that came before it and taken the lion share of the market from '
                       'Vue it\'s closest competitor.',
            'description': 'The Fashion',
            'field': 'Computer Science',
            'facilitators': [
                {
                    'name': 'Adewale Bukola',
                    'course_count': 2,
                    'student_count': 146789,
                    'id': '12'
                },
                {
                    'name': 'Dele Richards',
                    'course_count': 4,
                    'student_count': 146789,
                    'id': '13'
                }
            ],
            'language': 'English',
            'organization': 'Uwise',
            'skills': ['python', 'django', 'react', 'javascript', 'git', 'github', 'cloud'],
            'tags': ['python', 'django', 'react', 'git'],
            'objectives': [
                'Build your own web project in python',
                'Build a portfolio of web applications',
                'Interact with other students for networking',
                'Improve resume by getting professional help',
            ]
        }
    ]

}


class CourseView(TemplateView):
    template_name = 'course.html'

    def get(self, request, *args, **kwargs):
        course_data = None
        for course in dummy_data['courses']:
            # print(course.get('id'))
            if course.get('id') == kwargs['pk']:
                course_data = course
        # print(course_data)
        data = {
            'course_data': course_data,
            'testimonials': dummy_data['testimonials'],
            'page': 'course',
        }
        # print(data)
        context = {'data': data}
        return render(request, self.template_name, context)


class CourseListView(TemplateView):
    template_name = 'explore.html'

    def get(self, request, *args, **kwargs):
        data = dummy_data
        context = {'data': data}
        return render(request, self.template_name, context)


class EnrollView(TemplateView):
    template_name = 'enroll.html'

    def get(self, request, *args, **kwargs):
        course_data = None
        for course in dummy_data['courses']:
            # print(course.get('id'))
            if course.get('id') == kwargs['pk']:
                course_data = course
        # print(course_data)
        data = {
            'course_data': course_data,
            'testimonials': dummy_data['testimonials'],
            'page': 'enroll',
        }
        # print(data)
        context = {'data': data}
        return render(request, self.template_name, context)


class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        fields = courseAPI.models.Field.objects.all()
        testimonials = Testimonial.objects.all()
        carousels = CourseCarousel.objects.all()

        data = {
            'carousels': carousels,
            'testimonials': testimonials,
            'page': 'home',
            'fields': fields,
        }
        print(data)
        context = {'data': data}
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class PrivacyView(TemplateView):
    template_name = 'pages/privacy.html'


class ContactView(TemplateView):
    template_name = 'pages/contact.html'


class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and not self.request.user.is_superuser and not self.request.user.is_facilitator:
            return redirect('home')

        data = {
            'page': 'login',
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

        if user and not user.is_facilitator and not user.is_superuser:
            login(request, user)
            return redirect('home')
        else:
            return JsonResponse({'success': False, 'error': 'Invalid login credentials'})


class SignUpView(TemplateView):
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')

        data = {
            'page': 'signup',
        }
        context = {'data': data}
        return render(request, self.template_name, context)


def logout_user(request):
    logout(request)
    return redirect('login')
