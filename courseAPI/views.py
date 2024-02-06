from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *


# Create your views here.

class CourseLevelViewSet(ModelViewSet):
    queryset = CourseLevel.objects.all()
    serializer_class = CourseLevelSerializer
    permission_classes = [IsAdminUser]


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAdminUser]


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]


class AudioViewSet(ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    permission_classes = [IsAdminUser]


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAdminUser]


class FieldViewSet(ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [IsAdminUser]


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAdminUser]


class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAdminUser]


class FacilitatorAttendanceViewSet(ModelViewSet):
    queryset = FacilitatorAttendance.objects.all()
    serializer_class = FacilitatorAttendanceSerializer
    permission_classes = [IsAdminUser]


class StudentAttendanceViewSet(ModelViewSet):
    queryset = StudentAttendance.objects.all()
    serializer_class = StudentAttendanceSerializer
    permission_classes = [IsAuthenticated]


class AssessmentViewSet(ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [IsAdminUser]


class ResourceViewSet(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminUser]


class UserLessonViewSet(ModelViewSet):
    queryset = UserClass.objects.all()
    serializer_class = UserLessonSerializer
    permission_classes = [IsAuthenticated]

class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAdminUser]


class ReadingViewSet(ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
    permission_classes = [IsAdminUser]


class SpecializationViewSet(ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [IsAdminUser]


class SpecializationCourseViewSet(ModelViewSet):
    queryset = SpecializationCourse.objects.all()
    serializer_class = SpecializationCourseSerializer
    permission_classes = [IsAdminUser]


class UserCourseViewSet(ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer
    permission_classes = [IsAuthenticated]


class CourseFacilitatorViewSet(ModelViewSet):
    queryset = CourseFacilitator.objects.all()
    serializer_class = CourseFacilitatorSerializer
    permission_classes = [IsAdminUser]

