from django.db import models
from Courses.models import Course


class Moderator(models.Model):
    Login = models.CharField('User\'s name', max_length=20)
    Password = models.CharField('User password', max_length=30)
    courses = models.ManyToManyField(Course)

