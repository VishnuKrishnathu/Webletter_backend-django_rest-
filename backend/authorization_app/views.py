from django.shortcuts import render
from django.contrib.auth.models import User, auth


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from webletter_api.serializer import *
from webletter_api.models import *


# Create your views here.

@api_view([ 'POST'])
def loginData(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.data['username'], password = request.data['password'])
        if user:
            user_details = UsernameStorage.objects.get(username = request.data['username'])
            serializer = UsernameSerializer(user_details, many=False)
            return Response(serializer.data)
        else: 
            return Response({"username": False})
@api_view(['POST'])
def registerUser(request):
   if request.method=='POST':
       try:
            foreign_key=request.data['userdata']
            user_blog = BlogUsers.objects.get(id=foreign_key) 
            username = request.data['username']
            credentials = UsernameStorage(userdata = user_blog, username = username)  
            credentials.save()
            user = User.objects.create_user(username,request.data['email'], request.data['password'])
            user.first_name = request.data['firstname']
            user.last_name = request.data['lastname']
            user.save()
            return Response({"username": True,"password":True})
       except:
            return Response({
                    "username": False,
                    "password": False
                })
