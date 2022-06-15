from django.urls import path
from . import views

app_name = "hello"
urlpatterns = [
    path("", views.index, name="index"),
    path("brain", views.brain, name="brain"),
    path("<str:name>", views.greet, name="greet")
]