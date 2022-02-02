from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

# Create your views here.
from feed import models


class ProfileForm(forms.ModelForm):
    """Klasse zur Formularerstellung."""
    class Meta:
        model = models.Profile
        exclude = ['user']


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # Neuen User anlegen
            profile_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'auth/register.html', dict(form=user_form, profile_form=profile_form))
