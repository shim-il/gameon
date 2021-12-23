from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Not ready yet for full use.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class HighScore(models.Model):
    name = models.CharField(max_length=20)
    score = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name 

