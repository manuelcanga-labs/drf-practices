from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=25)
    fecha_creacion = models.DateField()

    class Meta:
        verbose_name = "equipo"
        verbose_name_plural = "equipos"

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    nickname = models.CharField(max_length=25)
    rol = models.CharField(max_length=25)
    
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="jugadores")

    class Meta:
        verbose_name = "jugador"
        verbose_name_plural = "equipos"

    def __str__(self):
        return self.nickname
