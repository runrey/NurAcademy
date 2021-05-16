from django.shortcuts import render
import requests


def moderating(request):
    url = 'http://127.0.0.1:8000/api/inactive-courses/'
    courses = requests.get(url=url).json()
    con = {
        'courses': courses,
    }
    return render(request, template_name='moderator/moderating.html', context=con)

