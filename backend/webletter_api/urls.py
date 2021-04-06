
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', homepage),
    path('api/', apiOverview , name ="api"),
    path('posts/', apiPostsView, name="posts"),
    path('api/<str:pk>/', apiSpecificUserFetch, name="specific_user"),
    path('posts/<str:pk>', apiSpecificPostFetch, name="specific_post")
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
