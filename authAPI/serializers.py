# serializers.py
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import *
from .views import *
from rest_framework.authtoken.models import Token


# serializers
class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        depth = 1


    def validate_password(self, value):
        """
        Validate the password using Django's password validation.
        """
        try:
            validate_password(value)
        except serializers.ValidationError as error:
            raise serializers.ValidationError(error.messages)

        return value

    def create(self, validated_data):
        """
        Create a user with the validated password.
        """
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user



class AcademicLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicLevel
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
        depth = 1


class OrganizationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationType
        fields = '__all__'


class AuthTokenWithEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(
        trim_whitespace=True,
        style={'input_type': 'email'})
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = User.objects.filter(email=email).first()

            if user and user.check_password(password):
                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled.')

                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError('Invalid email or password.')
        else:
            raise serializers.ValidationError('Must include "email" and "password".')


class AuthTokenWithUsernameSerializer(serializers.Serializer):
    username = serializers.CharField(trim_whitespace=True)
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):
                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled.')

                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError('Invalid username or password.')
        else:
            raise serializers.ValidationError('Must include "username" and "password".')
