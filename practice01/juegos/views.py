from django.shortcuts import render
from django.views.generic.list import ListView
from rest_framework.generics import ListCreateAPIView

from .models import Videojuego
from .serializers import VideojuegoSerializer

# Create your views here.
class Videojuegos(ListView):
    model = Videojuego
    template_name =  "juegos/lista_juegos.html"



class VideojuegosAPI(ListCreateAPIView):
    queryset = Videojuego.objects.all()
    serializer_class = VideojuegoSerializer