from rest_framework import serializers
from .models import BlogUsers, Posts

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogUsers
        fields = ['id', 'firstname', 'lastname', 'profilepicture', 'phonenumber', 'emailid']


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['posts', 'title', 'theme_image', 'article']