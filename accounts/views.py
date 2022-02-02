from django.shortcuts import render
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
        profileForm = ProfileForm(request.POST)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            return redirect('login')
    else:
        userForm = UserCreationForm()
        profileForm = ProfileForm()
    return render(request, 'registration/register.html', dict(form=userForm, profileForm=profileForm))

