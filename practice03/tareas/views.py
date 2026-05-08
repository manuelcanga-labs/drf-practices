from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Tarea
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

class TareaEndpoint(RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareasSerializer
    permission_classes = [IsAuthenticated]