from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from feed import models
from django.contrib.auth.decorators import login_required

from feed.models import Food, Profile


class FoodForm(forms.ModelForm):
    class Meta:
        model = models.Food
        exclude = [ 'user']


@login_required()
def upload(request):

    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FoodForm()
    return render(request, 'upload.html', dict(form=form))


def get_profile_posts(request):

    if request.method == "GET":
        user_id = request.GET.get('user')
        if user_id:
            foods = Food.objects.filter(user=int(user_id))
            profile = Profile.objects.filter(user=int(user_id))
        else:
            foods = []
            profile = []

        return render(request, 'profile.html', dict(
            foods=foods,
            profile=profile,
        ))
def get_all_posts(request):
    user_id = request.GET.get('user')


