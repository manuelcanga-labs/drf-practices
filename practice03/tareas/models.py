from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    completada = models.BooleanField(default=False)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tareas")

    def __str__(self):
        return self.titulo