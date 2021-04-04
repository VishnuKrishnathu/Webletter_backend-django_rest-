from rest_framework.authtoken import views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', views.obtain_auth_token),
    path('login/', loginData)
]