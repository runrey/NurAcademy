from django.shortcuts import render, redirect

from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import User, UserCourse, Course


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import UserSerializer, CourseSerializer, UserCourseSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'User List': 'user-list',
        'User view': '/user-detail/<str:pk>',
        'Create user': '/user-create/',
        'Update user': '/user-update/<str:pk>/',
        'Delete user': '/user-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def UserList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def CourseList(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def UserDetail(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def CourseDetail(request, pk):
    courses = Course.objects.get(id=pk)
    serializer = CourseSerializer(courses, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def UserCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    response = redirect('login')
    return response


@api_view(['POST'])
def CourseCreate(request):
    if request.session['email'] is None:
        return HttpResponse("You must be logged in first")
    else:
        m = User.objects.get(Email=request.session['email'])
        cserializer = CourseSerializer(data=request.data)
        if cserializer.is_valid():
            cserializer.save()

        usercourse = UserCourse(user_id=m.pk, course_id=cserializer.data['id'], Action=True)
        usercourse.save()
        return HttpResponse("You succeessfully created Course"+cserializer.data['Title'])


@api_view(['POST'])
def UserUpdate(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    response = redirect('apis:user-list')
    return response


@api_view(['POST'])
def CourseUpdate(request, pk):
    if request.session['email'] is None:
        return HttpResponse("You must be logged in first")

    course = Course.objects.get(id=pk)
    userID = UserCourse.objects.filter(course=pk, Action=True).values()[0][user_id]
    user = User.objects.get(id=userID)
    serializer = CourseSerializer(instance=course, data=request.data)

    if user.Email != request.session['email']:
        return HttpResponse("You don't have such permission")

    if serializer.is_valid():
        serializer.save()

    response = redirect('apis:course-list')
    return response


@api_view(['DELETE'])
def UserDelete(request, pk):
    if request.session['email'] is None:
        return HttpResponse("You must be logged in first")
    user = User.objects.get(id=pk)

    if user.Email != request.session['email']:
        return HttpResponse("You don't have such permission")

    user.delete()
    return Response("Item deleted!")


@api_view(['DELETE'])
def CourseDelete(request, pk):
    if request.session['email'] is None:
        return HttpResponse("You must be logged in first")

    course = Course.objects.get(id=pk)
    userID = UserCourse.objects.filter(course=pk, Action=True).values()[0]['user_id']

    user = User.objects.get(id=userID)
    if user.Email != request.session['email']:
        return HttpResponse("You don't have such permission")

    course.delete()
    return Response('Course deleted!')


@api_view(['POST'])
def Login(request):
    m = User.objects.get(Email=request.POST['email'])
    if m.Password == request.POST['pass']:
        request.session['email'] = m.Email
        request.session['username'] = m.Username
        response = redirect('index')
        return response
    else:
        response = redirect('login')
        return response


@api_view(['GET'])
def Logout(request):
    try:
        del request.session['email']
        del request.session['username']
    except KeyError:
        pass
    response = redirect('index')
    return response


