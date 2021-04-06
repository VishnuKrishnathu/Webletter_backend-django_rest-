from rest_framework import serializers
from .models import BlogUsers, Posts
from authorization_app.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogUsers
        fields = ['id', 'firstname', 'lastname', 'profilepicture', 'phonenumber', 'emailid']


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id','posts', 'title', 'theme_image', 'article']

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model= UsernameStorage
        fields = ['id', 'userdata','username']

class CredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
