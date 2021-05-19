from django.shortcuts import render
from django.http import HttpResponse, Http404
from .forms import UserForm
from .models import User


def index(request):
    return render(request, template_name='index.html')

def login(request):
    return render(request, template_name='login.html')

def sign(request):
    return render(request, template_name='sign.html')

def profile(request):

    user = User.objects.get(Email=request.session['email'])
    form = UserForm(initial=user.__dict__)

    context= {
        'form': form,
        'email': request.session['email']
    }
    return render(request, template_name='profile.html', context=context)

def my_courses(request):
    return render(request, template_name='my_courses.html')

