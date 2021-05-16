from django.shortcuts import render, redirect

from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import User, UserCourse, Course, Module

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import UserSerializer, CourseSerializer, UserCourseSerializer, ModuleSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'User List': 'user-list',
        'User view': '/user-detail/<str:pk>',
        'Create user': '/user-create/',
        'Update user': '/user-update/<str:pk>/',
        'Delete user': '/user-delete/<str:pk>/',
        'Course List': 'course-list',
        'Course view': '/course-detail/<str:pk>',
        'Create course': '/course-create/',
        'Update course': '/course-update/<str:pk>/',
        'Delete course': '/course-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def UserList(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    except Exception as e:
        return HttpResponse(Http404("Users does not exist"))


@api_view(['GET'])
def CourseList(request):
    try:
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    except Exception as e:
        return HttpResponse(Http404("Poll does not exist"))

@api_view(['GET'])
def InactiveCourseList(request):
    try:
        courses = Course.objects.filter(Status='IA')#.prefetch_related('usercourse_set__user')
        # users = User.objects.prefetch_related('usercourse_set__course')
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return HttpResponse(Http404("Poll does not exist"))


@api_view(['GET'])
def UserDetail(request, pk):
    try:
        users = User.objects.get(id=pk)
        serializer = UserSerializer(users, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response(Http404)

@api_view(['GET'])
def CourseDetail(request, pk):
    try:
        courses = Course.objects.get(id=pk)
        serializer = CourseSerializer(courses, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response(Http404)

@api_view(['GET'])
def ModuleDetail(request, pk):
    try:
        module = Module.objects.get(id=pk)
        serializer = ModuleSerializer(module, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response(Http404)


@api_view(['POST'])
def UserCreate(request):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        response = redirect('login')
        return response
    except Exception as e:
        return Response(Http404)


@api_view(['POST'])
def CourseCreate(request):
    try:
        mail = request.session['email']
        if mail is None:
            raise Exception

        m = User.objects.get(Email=mail)
        cserializer = CourseSerializer(data=request.data)
        ans = False
        if cserializer.is_valid():
            cserializer.save()
            ans = True

        usercourse = UserCourse(user_id=m.pk, course_id=cserializer.data['id'], Action=True)
        usercourse.save()
        return HttpResponse(ans)
    except Exception as e:
        return HttpResponse("You must be logged in first")

@api_view(['POST'])
def ModuleCreate(request):
    try:

        cserializer = ModuleSerializer(data=request.data)
        if cserializer.is_valid():
            cserializer.save()

        return HttpResponse(ans)
    except Exception as e:
        return HttpResponse("You must be logged in first")


@api_view(['POST'])
def UserUpdate(request, email):

    try:
        mail = request.session['email']
        if mail is None or mail != email:
            raise Exception

        user = User.objects.get(Email=email)
        serializer = UserSerializer(instance=user, data=request.data)
        ans = False
        if serializer.is_valid():
            ans = True
            serializer.save()

        return Response(ans)
    except Exception as e:
        return Response(Http404)


@api_view(['POST'])
def CourseUpdate(request, pk):
    return Response(request.data)
    # try:
    #     mail = request.session['email']
    #     if mail is None:
    #         raise Exception
    #
    #     course = Course.objects.get(id=pk)
    #     serializer = CourseSerializer(instance=course, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return HttpResponse(True)
    #     return HttpResponse(False)
    # except Exception as e:
    #     return HttpResponse("You must be logged in first")

@api_view(['POST'])
def ModuleUpdate(request, pk):
    try:
        module = Module.objects.get(id=pk)
        serializer = ModuleSerializer(instance=course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(True)
        return HttpResponse(False)
    except Exception as e:
        return HttpResponse("You must be logged in first")


@api_view(['DELETE'])
def UserDelete(request, pk):
    try:
        mail = request.session['email']
        user = User.objects.get(id=pk)
        if mail is None or user.Email != request.session['email']:
            raise Exception
        user.delete()
        return Response(True)
    except Exception as e:
        return Response(Http404)



@api_view(['DELETE'])
def CourseDelete(request, pk):
    try:
        mail = request.session['email']
        course = Course.objects.get(id=pk)
        userID = UserCourse.objects.filter(course=pk, Action=True).values()[0]['user_id']

        user = User.objects.get(id=userID)

        if user.Email != mail or mail is None:
            raise Exception

        course.delete()
        return Response('Course deleted!')
    except Exception as e:
        return Response(Http404)

@api_view(['DELETE'])
def ModuleDelete(request, pk):
    try:
        module = Module.objects.get(id=pk)
        module.delete()
        return Response(True)
    except Exception as e:
        return Response(False)


@api_view(['POST'])
def Login(request):
    try:
        m = User.objects.get(Email=request.POST['email'])
        if m.Password == request.POST['pass']:
            request.session['email'] = m.Email
            request.session['username'] = m.Username
            response = redirect('index')
            return response
        else:
            response = redirect('login')
            return response
    except Exception as e:
        return Response(Http404)


@api_view(['GET'])
def Logout(request):
    try:
        request.session['email'] = None
        request.session['username'] = None
    except KeyError:
        pass
    response = redirect('index')
    return response


@api_view(['GET'])
def modules(request, course_id):
    try:
        modules = Module.objects.filter(course_id=course_id)
        ser = ModuleSerializer(instance=modules, many=True)
        return Response(ser.data)
    except Exception as e:
        return Response(Http404)
    finally:
        pass

