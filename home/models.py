from operator import truediv
from unittest.util import _MAX_LENGTH
from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_craecion = models.DateField(null=True)
   
    # comidafav = models.CharField(max_length=30)
