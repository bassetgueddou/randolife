from django.contrib.auth.models import User
from django.db import models


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
