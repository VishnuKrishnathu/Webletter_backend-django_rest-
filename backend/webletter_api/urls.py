
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', homepage),
    path('api/', apiOverview , name ="api"),
    path('posts/', apiPostsView, name="posts"),
    path('api/<str:pk>/', apiUserFetch, name="pk")
]