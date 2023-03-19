from django.urls import path
from . import views
from . import api

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("creer/", views.CreerActiviteView.as_view(), name="creer"),
    path("api/activites/", api.ActiviteList.as_view(), name="api_activites"),
    path("api/activites/<int:pk>/", api.ActiviteDetail.as_view(),
         name="api_activite_detail"),
]
