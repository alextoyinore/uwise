from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authAPI.models import Facilitator
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

    def create(self, request, *args, **kwargs):
        facilitator_exists = Facilitator.objects.filter(username=self.request.data['username']).exists()
        level_exists = CourseLevel.objects.filter(title=self.request.data['title']).exists()

        if not facilitator_exists:
            return Response({'message': 'Facilitator does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        elif not level_exists:
            return Response({'message': 'Invalid Course Level'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = CourseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()


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


class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAdminUser]


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
