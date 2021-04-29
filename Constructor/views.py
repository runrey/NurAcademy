from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewCourseForm
from .models import Course,UserCourse, User
def mainPage(request):
    try:
        mail = request.session['email']
        if mail is None:
            raise Exception
        courses = Course.objects.filter(usercourse__user__Email=mail)
        context = {
            'courses': courses,
        }
        return render(request=request, template_name='constructor/mainPage.html', context=context)
    except Exception as e:
        print(e)
        return redirect('login')


def newCourse(request):
    form = NewCourseForm()
    context = {
        'form': form,
    }
    return render(request=request, template_name='constructor/newcourse.html', context=context)


def updateMyCourse(request, course_id):
    try:
        course = Course.objects.get(id=course_id, usercourse__user__Email=request.session['email'], usercourse__Action=True)
    except Exception as e:
        return HttpResponse("It is none of your bussiness")

    data = course.__dict__
    form = NewCourseForm(initial=data)
    context = {
        'form': form,
        'course_id': course.id
    }
    return render(request=request,template_name='constructor/updatecourse.html', context=context)

