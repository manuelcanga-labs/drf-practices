from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Tarea

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'email', 'username', 'password',)
        extra_kwargs = {
            'password': {"write_only": True},
        }


class TareasSerializer(serializers.ModelSerializer):
    # serializers.ReadOnlyField(source='propietario.id')

    class Meta:
        model = Tarea
        fields = ('titulo', 'completada', 'propietario',)
        read_only_fields = ('propietario',)