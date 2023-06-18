from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("notebook", views.notebook, name="notebook"),
    path("notebook/<int:id>", views.notebook_details, name="details"),
    path("notebook-min", views.notebook_min, name="min"),
    path("notebook-max", views.notebook_max, name="max"),
    path("notebook-puan", views.notebook_puan, name="puan"),
    path("search_venues",views.search_venues,name = "search-venues")
]
