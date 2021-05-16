from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .forms import CourseForm, ModuleForm
from .models import Course,UserCourse, User, Module
import requests


def mainPage(request):
    try:
        mail = request.session['email']
        if mail is None:
            raise Exception
        courses = Course.objects.filter(usercourse__user__Email=mail, usercourse__Action=True)
        context = {
            'courses': courses,
        }
        return render(request=request, template_name='constructor/mainPage.html', context=context)
    except Exception as e:
        print(e)
        return redirect('login')


def newCourse(request):
    form = CourseForm()
    context = {
        'form': form,
    }
    return render(request=request, template_name='constructor/newcourse.html', context=context)


def updateMyCourse(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        check = UserCourse.objects.get(user__Email=request.session['email'], course_id=course_id, Action=True)
        url = 'http://127.0.0.1:8000/api/course-modules/' + course_id
        modules = requests.get(url=url).json()
        forms = []
        for module in modules:
            forms.append(ModuleForm(initial={'Module_title': module['Module_title'], 'Content': module['Content']}))

    except Exception as e:
        print(e)
        return HttpResponse("It is none of your bussiness")

    data = course.__dict__
    form = CourseForm(initial=data)

    context = {
        'form': form,
        'course_id': course.id,
        'forms': forms,
    }

    return render(request=request,template_name='constructor/updatecourse.html', context=context)

