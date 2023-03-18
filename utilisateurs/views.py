from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class InscriptionView(CreateView):
    template_name = "utilisateurs/inscription.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("activites:index")


class ConnexionView(LoginView):
    template_name = "utilisateurs/connexion.html"
    success_url = reverse_lazy("activites:index")


class DeconnexionView(LogoutView):
    next_page = reverse_lazy("activites:index")
