from django.db.models.signals import post_save
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from feed import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from feed.models import Food, Profile
from foodies2 import settings


class FoodForm(forms.ModelForm):
    """Klasse zur Formularerstellung."""
    class Meta:
        model = models.Food
        exclude = ['user']



def homepage(request):
    user_id = request.GET.get('user')
    if user_id:
        foods = models.Food.objects.all()
        profiles = models.Profile.objects.all()
        users = models.User.objects.all()
    else:
        foods = []
        profiles = []
        users = []

    return render(request, 'index.html', dict(
        foods=foods,
        profiles=profiles,
        users=users,
    ))
    




# für die folgenenden Views muss man angemeldet sein

@login_required()
def upload(request):
    # werden Formulardaten geschickt?
    print("hallo")
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():  # Formular überprüfen
            form.save()
            return HttpResponseRedirect('feed')  # Umleitung
    else:
        form = FoodForm()  # leeres Formular
    return render(request, 'upload.html', dict(form=form))



# Löscht Foodpost und gibt alle anderen zurück

@login_required()
def delete(request):
    if request.method == "POST":
        user_id = request.GET.get('user')
        search_query = Food.objects.filter(id=request.data.get(id))
        food_to_delete = search_query[0]

        if food_to_delete.user.id == int(user_id):
            food_to_delete.delete()
        else:
            food_to_delete = []
        return render(request, 'profile.html', dict(
            foods=Food.objects.all()
        ))


# gibt daten des Profils und alle Foodposts der Ersteller*in zurück
@login_required()
def get_profile_posts(request):
    if request.method == "GET":
        user_id = request.GET.get('user')
        if user_id:
            foods = Food.objects.filter(user=int(user_id))
            profile = Profile.objects.filter(user=int(user_id))
            user = User.objects.filter(request.get('user'))
        else:
            foods = []
            profile = []
            user = []

        return render(request, 'profile.html', dict(
            foods=foods,
            profile=profile,
            user=user,
        ))


# gibt alle Food posts zurück



# aus der Vorlesung

'''
def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
'''



