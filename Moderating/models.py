from django.db import models
from Courses.models import Course
# from Courses.models import User, UserCourse, Course, Module


class Moderator(models.Model):
    Login = models.CharField('User\'s name', max_length=20, unique=True)
    Password = models.CharField('User password', max_length=30)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.Login

