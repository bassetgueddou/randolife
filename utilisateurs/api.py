from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer

# Créez une vue pour gérer la création d'un nouvel utilisateur


class CustomUserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
