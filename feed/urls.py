from django.urls import path

from .views import homepage, upload, get_profile_posts

urlpatterns =[
    path('', homepage, name='homepage'),
    path('profile',get_profile_posts ,name='profile'),
    path('upload', upload, name='upload')
]
