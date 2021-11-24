from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="encyclopedia-index"),
    path("wiki/<str:title>", views.wiki, name="encyclopedia-wiki"),
    path("creation", views.creation, name="encyclopedia-creation")
]