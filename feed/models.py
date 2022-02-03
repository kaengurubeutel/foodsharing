from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    avatar = models.ImageField("Avatar", upload_to="avatar", blank=True, null= True)
    email = models.CharField('email', max_length=20, default="Test@email.de")
    hometown = models.CharField('hometown', max_length=20, default="Bielefeld")


class Food(models.Model):
    image = models.ImageField("Img", upload_to="food", blank= True, null= True)
    description = models.TextField('description',max_length=200, default = " ")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return {self.description}
