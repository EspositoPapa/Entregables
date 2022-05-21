from datetime import datetime
from django.db import models
import datetime


# Create your models here.
#BD con informacion de la familia#
class Familia (models.Model):
    Nombre=models.CharField(max_length=40)#Caracteres(string corto)#
    Apellido=models.CharField(max_length=30)
    Edad=models.IntegerField()
    Parentesco=models.CharField(max_length=30)
    Direccion=models.CharField(max_length=40)
    Email=models.EmailField(max_length=50)

#BD con la fecha de ingreso al sistema#
class IngresoenSistema (models.Model):
    NomFam=models.CharField(max_length=40)
    FingresoSist=models.DateField(default=datetime.datetime.now())
    FamDirecto=models.BooleanField()

