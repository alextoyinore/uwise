from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from uwise.permissions import IsFacilitator, IsStudent, IsUwiseAdmin

from .serializers import *

# Create your views here.

class CourseLevelViewSet(ModelViewSet):
    queryset = CourseLevel.objects.all()
    serializer_class = CourseLevelSerializer
    permission_classes = [IsAdminUser]


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser, IsFacilitator, IsUwiseAdmin, IsStudent]

    def create(self, request, *args, **kwargs):
        if 'image' in request.data:
            image = request.data['image']
            return super().create(request, image=image, *args, **kwargs)
        else:
            return super().create(request, *args, **kwargs)


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAdminUser, IsFacilitator, IsStudent]


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser, IsFacilitator, IsStudent]


class AudioViewSet(ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    permission_classes = [IsAdminUser, IsFacilitator, IsStudent]


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAdminUser, IsFacilitator, IsStudent]


class FieldViewSet(ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [IsAdminUser, IsUwiseAdmin]


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAdminUser, IsFacilitator, IsStudent]


class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAdminUser, IsFacilitator, IsStudent]


class FacilitatorAttendanceViewSet(ModelViewSet):
    queryset = FacilitatorAttendance.objects.all()
    serializer_class = FacilitatorAttendanceSerializer
    permission_classes = [IsAdminUser, IsFacilitator]


class StudentAttendanceViewSet(ModelViewSet):
    queryset = StudentAttendance.objects.all()
    serializer_class = StudentAttendanceSerializer
    permission_classes = [IsAuthenticated, IsStudent]


class AssessmentViewSet(ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [IsAdminUser, IsFacilitator, IsStudent]


class ResourceViewSet(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminUser, IsFacilitator, IsStudent]


class UserClassesViewSet(ModelViewSet):
    queryset = UserClass.objects.all()
    serializer_class = UserLessonSerializer
    permission_classes = [IsAuthenticated, IsStudent]


class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAdminUser, IsFacilitator, IsStudent]


class ReadingViewSet(ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
    permission_classes = [IsAdminUser, IsFacilitator, IsStudent]


class SpecializationViewSet(ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [IsAdminUser, IsUwiseAdmin]


class SpecializationCourseViewSet(ModelViewSet):
    queryset = SpecializationCourse.objects.all()
    serializer_class = SpecializationCourseSerializer
    permission_classes = [IsAdminUser, IsUwiseAdmin]


class UserCourseViewSet(ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer
    permission_classes = [IsAuthenticated]


class CourseFacilitatorViewSet(ModelViewSet):
    queryset = CourseFacilitator.objects.all()
    serializer_class = CourseFacilitatorSerializer
    permission_classes = [IsAdminUser, IsUwiseAdmin, IsFacilitator]

