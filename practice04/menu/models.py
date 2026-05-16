from django.db import models

# Create your models here.
class RecetaSecreta(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.TextField()
    
    def __str__(self):
        return self.nombre


