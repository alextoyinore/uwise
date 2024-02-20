from rest_framework import serializers
from .models import *


# serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'