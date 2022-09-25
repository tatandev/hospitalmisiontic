from django.db import models
from .auxiliar import Auxiliar
from .user import User


class Enfermero(models.Model):
     id = models.AutoField(primary_key=True)
     rh = models.CharField(max_length=45)
     especialidad = models.CharField(max_length=45)
     auxiliar = models.ForeignKey(Auxiliar,related_name='enfermero', on_delete=models.CASCADE,null=True)
     usuario = models.ForeignKey(User,related_name='enfermero', on_delete=models.CASCADE)