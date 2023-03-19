from rest_framework import serializers
from .models import Activite


class ActiviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activite
        fields = ['id', 'nom', 'description', 'date',
                  'lieu', 'createur', 'participants']
