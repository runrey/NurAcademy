from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import UserForm
from .models import User, Course, UserCourse


def index(request):
    return render(request, template_name='index.html')


def login(request):
    return render(request, template_name='login.html')


def sign(request):
    return render(request, template_name='sign.html')


def profile(request):
    user = User.objects.get(Email=request.session['email'])
    form = UserForm(initial=user.__dict__)

    context = {
        'form': form,
        'email': request.session['email']
    }
    return render(request, template_name='profile.html', context=context)


def my_courses(request):
    courses = Course.objects.filter(usercourse__user__Email=request.session['email'], usercourse__Action=True)
    courses_2 = Course.objects.filter(usercourse__user__Email=request.session['email'], usercourse__Action=False)
    if len(courses) > 0 and len(courses_2) > 0:
        context = {
            'courses': courses,
            'courses_2': courses_2
        }
    elif len(courses) > 0 and len(courses_2) <= 0:
        context = {
            'courses': courses,
            'courses_2': 0
        }
    elif len(courses) <= 0 and len(courses_2) > 0:
        context = {
            'courses': 0,
            'courses_2': courses_2
        }
    else:
        context = {
            'courses': 0,
            'courses_2': 0
        }

    return render(request=request, template_name='my_courses.html', context=context)

def courses(request):
    courses = Course.objects.all()
    if len(courses) > 0:
        context = {
            'courses': courses,
        }
    else:
        context = {
            'courses': 0,
        }

    return render(request=request, template_name='courses.html', context=context)
