from django.urls import path

from .views import homepage, get_all_posts, upload

urlpatterns =[
    path('', homepage, name='homepage'),
    path('feed/', get_all_posts, name='feed'),
    path('upload/', upload, name='upload')
]