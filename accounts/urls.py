from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register


urlpatterns =[
    path('register', register, name='register_url'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(), name="login"),
]