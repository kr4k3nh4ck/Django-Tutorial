from django.urls import path, include
from . import views

urlpatterns = [
path("start/", views.index),
path("<int:id>", views.index2),
path("", views.home),
path("create/", views.create),
path("view/", views.view),
]