from rest_framework import serializers
from .models import User, Course, UserCourse, Module, Moderator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['Username', 'Email', 'Password']

        # def create(self, validated_data):
        #     user = User
        #     return user







