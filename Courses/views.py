from django.shortcuts import render
from django.http import HttpResponse, Http404
from . import models


def index(request):
    return render(request, template_name='index.html')

def login(request):
    return render(request, template_name='login.html')

