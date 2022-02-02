from django.forms import forms
from django.shortcuts import render
from accounts import models
from django.contrib.auth.decorators import login_required


class FoodForm(forms.ModelForm):
    class Meta:
        model = models.Food
        exclude = [ 'user']

@login_required()
def feed(request):
    all
