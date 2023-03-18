from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views import generic
from .models import Activite


class IndexView(generic.ListView):
    template_name = "activites/index.html"
    context_object_name = "activites"

    def get_queryset(self):
        return Activite.objects.order_by("-date")


class DetailView(generic.DetailView):
    model = Activite
    template_name = "activites/detail.html"


class CreerActiviteView(generic.CreateView):
    model = Activite
    fields = ["titre", "description", "date", "lieu", "categorie"]
    template_name = "activites/creer_activite.html"
    succes_url = reverse_lazy("activites:index")


def liste_activites(request):
    activites_list = Activite.objects.all()
    paginator = Paginator(activites_list, 10)  # 10 activités par page

    page = request.GET.get('page')
    activites = paginator.get_page(page)

    return render(request, 'activites/liste_activites.html', {'activites': activites})
