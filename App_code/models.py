from django.db import models

# Create your models here.
class Familiares(models.Model):
    tipo_f = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)    
    edad = models.IntegerField()
    estado_f = models.CharField(max_length=50)