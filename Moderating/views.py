from django.shortcuts import render
import requests
from Courses.models import User, UserCourse, Course


def moderating(request):
    courses = Course.objects.filter(Status='IA')
    coursesNEW = {}
    for course in courses:
        usrCourse = UserCourse.objects.filter(course=course).first()
        if usrCourse.Action:
            coursesNEW[course] = usrCourse.user.Username
    con = {
        'courses': coursesNEW,
    }

    return render(request, template_name='moderator/moderating.html', context=con)