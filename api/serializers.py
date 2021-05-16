from rest_framework import serializers
from .models import User, Course, UserCourse, Module, Moderator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['Username', 'Email', 'Password']
        read_only = ['pk']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        # fields = ['Title', 'Description', 'Status']
        # read_only = ['pk']


class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        # fields = '__all__'
        fields = ['course', 'user', 'Action']

class ModuleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Module
            fields = '__all__'







