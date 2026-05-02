from rest_framework import generics

from .models import Equipo
from .serializers import EquipoSerializer

# Create your views here.
class EquipoListCreate(generics.ListCreateAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


class EquipoRetrieve(generics.RetrieveAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

