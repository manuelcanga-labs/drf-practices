from django.views.generic.base import TemplateView
from rest_framework import generics

from .models import Equipo
from .serializers import EquipoSerializer


class HomePage(TemplateView):
    template_name = "liga/frontend.html"


# Create your views here.
class EquipoListCreate(generics.ListCreateAPIView):
    queryset = Equipo.objects.prefetch_related("jugadores")
    serializer_class = EquipoSerializer


class EquipoRetrieve(generics.RetrieveAPIView):
    queryset = Equipo.objects.prefetch_related("jugadores")
    serializer_class = EquipoSerializer