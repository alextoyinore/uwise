from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from utilsAPI.models import Category
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


class GenderViewSet(ModelViewSet):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]



class GradeViewSet(ModelViewSet):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class AnnouncementViewSet(ModelViewSet):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

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


class FavouriteViewSet(ModelViewSet):
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()
    permission_classes = [IsAuthenticated]
