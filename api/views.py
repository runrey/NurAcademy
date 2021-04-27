from django.shortcuts import render, redirect

from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import User


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import UserSerializer


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
def UserDetail(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def UserCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    response = redirect('apis:user-list')
    return response


@api_view(['POST'])
def UserUpdate(request, pk):

    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

    response = redirect('apis:user-list')
    return response


@api_view(['DELETE'])
def UserDelete(request, pk):
    user = user.objects.get(id=pk)
    user.delete()
    return Response("Item deleted!")


