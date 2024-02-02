from django.forms import ModelForm, PasswordInput, TextInput, EmailInput
from djoser.conf import User


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        # extra_kwargs = {'password': {'widget': PasswordInput},
        #                 'first_name': {'widget': TextInput(attrs={''})},
        #                 'last_name': {'widget': TextInput(attrs={''})},
        #                 'email': {'widget': EmailInput(attrs={''})}}


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        # extra_kwargs = {'password': {'widget': PasswordInput},
        #                 'email': {'widget': EmailInput(attrs={''})}}
