from rest_framework import serializers
from .models import CustomUser

# Créez un serializer pour le modèle CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password',
                  'date_naissance', 'photo_profil', 'preferences']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}
