from rest_framework import serializers
from .models import CustomUserModel


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'email', 'password',
                  'date_naissance', 'photo_profil', 'preferences']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}
