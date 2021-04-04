from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from webletter_api.serializer import *


# Create your views here.

@api_view(['GET', 'POST'])
def loginData(request):
    if request.method == 'POST':
        try:
            username = User.objects.get(username = request.data['username'])
            serializer = CredentialsSerializer( username, many=False)
            if (serializer.data['password']== request.data['password']):
                return Response(serializer.data)
            else:
                return Response()    
        except:
            return Response({
                'username': False,
                'password': False
            })
    else:
        user = User.objects.all()
        serializer = CredentialsSerializer(user, many=True)
        return Response(serializer.data)
    