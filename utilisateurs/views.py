from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class InscriptionView(auth_views.CreateView):
    template_name = "utilisateurs/inscriptions.html"
    form_class = UserCreationForm
    succes_url = reverse_lazy("activites:index")


class ConnexionView(auth_viewq.loginView):
    template_name = "utilisateurs/connexion.html"
    succes_url = reverse_lazy("activities:index")


class DeconnexionView(auth_views.LoginView):
    next_page = reverse_lazy("activites:index")
