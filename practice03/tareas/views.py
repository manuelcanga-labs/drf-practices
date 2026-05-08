from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Tarea
from .permissions import EsPropietario
from .serializers import UserSerializer, TareasSerializer


# Create your views here.
class CreateUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class TareasEndpoint(ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareasSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(propietario=self.request.user)

    def get_queryset(self):
        return super().get_queryset().filter(propietario=self.request.user)

class TareaEndpoint(RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareasSerializer
    permission_classes = [EsPropietario]

    def perform_create(self, serializer):
        serializer.save(propietario=self.request.user)