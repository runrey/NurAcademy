from django.shortcuts import render

def moderating(request):
    return render(request, template_name='moderator/moderating.html')


