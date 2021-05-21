from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .forms import CourseForm, ModuleForm
from .models import Course,UserCourse, User, Module
from django.forms import modelformset_factory, HiddenInput
import requests

ModuleFormSet = modelformset_factory(Module, fields=('Module_title', 'Content', 'course'))

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
        if request.method == 'POST':
            formset = ModuleFormSet(request.POST)
            if formset.is_valid():
                formset.save()
    except Exception as e:
        pass

    try:
        formset = ModuleFormSet(queryset=Module.objects.filter(course_id=course_id))
        course = Course.objects.get(id=course_id)

        for form in formset:
            form.fields['course'].widget = HiddenInput()
            form.fields['course'].initial = course_id

        context = {
            'course': course,
            'forms': formset,
        }

        return render(request=request,template_name='constructor/updatecourse.html', context=context)
    except Exception as e:
        print(e)
        return HttpResponse("It is none of your bussiness")

def test(request):
    pass
