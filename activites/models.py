from django.db import models
from utilisateurs.models import Profil


class Activite(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    participants = models.ManyToManyField(Profil, related_name='activites')
    categorie = models.CharField(max_length=255)
    image = models.ImageField(upload_to='activites/', blank=True, null=True)

    def __str__(self):
        return self.titre
