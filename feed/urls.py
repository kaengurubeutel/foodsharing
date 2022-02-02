from django.urls import path

from .views import homepage, feed

urlpatterns =[
    path('', homepage, name='homepage'),
    path('feed/', feed, name='feed'),
]