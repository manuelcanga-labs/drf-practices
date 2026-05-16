from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import RecetaSecreta
from .serializers import RecetaSecretaSerializer

# Create your views here.
class Recetas(ListCreateAPIView):
    queryset = RecetaSecreta.objects.all()
    serializer_class = RecetaSecretaSerializer
    permission_classes = [IsAuthenticated,]

