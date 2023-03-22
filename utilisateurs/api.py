from rest_framework import generics
from .models import CustomUserModel
from .serializers import CustomUserSerializer

# Créez une vue pour gérer la création d'un nouvel utilisateur


class CustomUserCreate(generics.CreateAPIView):
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer
