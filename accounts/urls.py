from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, createprofile


urlpatterns =[
    path('register', register, name='register_url'),
    path('profile', createprofile, name='profile'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(), name="login"),
]