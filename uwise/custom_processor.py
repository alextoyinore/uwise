from django.contrib.auth.base_user import AbstractBaseUser
from django.http import request


class CustomUserProcessor(AbstractBaseUser):
    @property
    def is_logged_in(self) -> bool:
        if request.COOKIES.get('uwiseweb'):
            super.is_authenticated = True
            return super.is_authenticated
