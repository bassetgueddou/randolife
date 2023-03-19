from django.urls import path
from . import views
from . import api

urlpatterns = [
    path("inscription/", views.InscriptionView.as_view(), name="inscription"),
    path("connexion/", views.ConnexionView.as_view(), name="connexion"),
    path("deconnexion/", views.DeconnexionView.as_view(), name="deconnexion"),
    path("api/inscription/", api.CustomUserCreate.as_view(), name="api_inscription"),
]
