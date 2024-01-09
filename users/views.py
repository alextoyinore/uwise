from django.shortcuts import render
from users import serializers
from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from social_django.utils import psa


# views.py
class UserView(ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        # Applying different permissions for different methods
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]


class GenderView(ModelViewSet):
    serializer_class = serializers.GenderSerializer
    queryset = Gender.objects.all()
    permission_classes = [IsAdminUser]

class UserGenderView(ModelViewSet):
    serializer_class = serializers.UserGenderSerializer
    queryset = UserGender.objects.all()
    permission_classes = [IsAdminUser]


class AcademicLevelView(ModelViewSet):
    serializer_class = serializers.AcademicLevelSerializer
    queryset = AcademicLevel.objects.all()
    permission_classes = [IsAdminUser]


class UserAcademicLevelView(ModelViewSet):
    serializer_class = serializers.UserAcademicLevelSerializer
    queryset = UserAcademicLevel.objects.all()


class OrganizationView(ModelViewSet):
    serializer_class = serializers.OrganizationSerializer
    queryset = Organization.objects.all()


class OrganizationTypeView(ModelViewSet):
    serializer_class = serializers.OrganizationTypeSerializer
    queryset = OrganizationType.objects.all()
    permission_classes = [IsAdminUser]


class LoginWithEmailView(ObtainAuthToken):
    serializer_class = serializers.AuthTokenWithEmailSerializer


class LoginWithUsernameView(ObtainAuthToken):
    serializer_class = serializers.AuthTokenWithUsernameSerializer


class ProfileView(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, **kwargs):
        current_user = request.user
        serialized_user = serializers.UserSerializer(current_user)
        return Response(serialized_user.data)


class LogoutView(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, **kwargs):
        request.auth.delete()
        return Response({"message": "You logged out!"}, status=status.HTTP_200_OK)


class SocialLoginView(ModelViewSet):
    @psa('social:complete')
    def create(self, request, backend):
        user = request.user
        serialized_user = serializers.UserSerializer(user)
        return Response({'message': 'Login successful!', 'user': serialized_user.data})
