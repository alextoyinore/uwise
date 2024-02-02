# authentication_backends.py

from django.contrib.auth.backends import BaseBackend
from authAPI.models import User
from rest_framework.authtoken.models import Token


class TokenAuthenticationBackend(BaseBackend):
    def authenticate(self, request, token=None):
        # Implement logic to authenticate the user based on the token
        # For simplicity, let's assume you have a User model with a 'token' field
        try:
            user = Token.objects.get(key=token)
            return user
        except Token.DoesNotExist:
            return None

    def get_user(self, user_id):
        # Implement logic to retrieve the user
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

