from django.urls import path

from .views import Recetas

urlpatterns = [
    path("recetas/", Recetas.as_view(), name="recetas"),
]
