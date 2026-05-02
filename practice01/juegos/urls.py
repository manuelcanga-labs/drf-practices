from django.urls import path


from .views import Videojuegos, VideojuegosAPI


urlpatterns = [
    path("", Videojuegos.as_view(), name="home"),
    path("juegos", VideojuegosAPI.as_view(), name="juegos"),
]
