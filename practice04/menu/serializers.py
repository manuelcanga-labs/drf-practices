from rest_framework import serializers
from .models import RecetaSecreta


class RecetaSecretaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RecetaSecreta
        fields = ("nombre", "ingredientes",)
    
