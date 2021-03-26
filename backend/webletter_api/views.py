from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer, PostsSerializer
from .models import *


# Create your views here.
@api_view(['GET', 'POST'])
def apiOverview(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    else:
        users = BlogUsers.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


def homepage(request):
    return HttpResponse("<h1>Hello World</h1>")


@api_view([ 'GET', 'POST' ])
def apiPostsView(request):
    if request.method == 'POST':
        serializer = PostsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        posts= Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def apiSpecificUserFetch(request, pk):
    if request.method == 'POST':
        user = BlogUsers.objects.get(id=pk)
        serializer = UserSerializer(instance = user, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    else:
        users = BlogUsers.objects.get(id=pk)
        serializer = UserSerializer(users, many=False)
        return Response(serializer.data)

