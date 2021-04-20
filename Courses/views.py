from django.shortcuts import render
from django.http import HttpResponse, Http404
from . import models


def index(request):
    ss = models.Course.objects.all()
    ans = ''
    for i in ss:
        ans += str(i) + '<br><br>'
    print(ans)

    return HttpResponse(ans)


