from rest_framework import generics
from .models import Activite
from .serializers import ActiviteSerializer

# Créez une vue pour lister toutes les activités


class ActiviteList(generics.ListAPIView):
    queryset = Activite.objects.all()
    serializer_class = ActiviteSerializer

# Créez une vue pour récupérer, mettre à jour et supprimer une activité spécifique


class ActiviteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activite.objects.all()
    serializer_class = ActiviteSerializer
