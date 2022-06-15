from django.urls import path

from . import views

app_name = "newyears"
urlpatterns = [
    path("", views.index, name="index")
]