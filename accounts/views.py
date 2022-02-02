from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

# Create your views here.
from feed import models

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        exclude = ['user']

def register(request):
    if request.method == 'POST':
        userForm = UserCreationForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            return redirect('profile')
    else:
        userForm = UserCreationForm()
    return render(request, 'auth/register.html', dict(form=userForm))


def createprofile(request):
    if request.method == 'POST':
        profileform= ProfileForm(request.POST)
        if profileform.is_valid():
            profileform.save()
            return redirect('login')
        else:
            profileForm = ProfileForm()
        return render (request, 'auth/profile.html', dict(form=profileForm))
