from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from utilsAPI.models import Category
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser]


class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminUser]


class GenderViewSet(ModelViewSet):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()
    permission_classes = [IsAdminUser]


class GradeViewSet(ModelViewSet):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class RatingViewSet(ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

