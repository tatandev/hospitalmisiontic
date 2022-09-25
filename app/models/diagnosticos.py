from django.db import models
from .medico import Medico
from .paciente import Paciente


class Diagnostico (models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    prioridad = models.CharField(max_length=45)
    fecha_registro = models.DateField()
    medico = models.ForeignKey(Medico,related_name='diagnostico', on_delete=models.CASCADE,null=True)
    paciente = models.ForeignKey(Paciente,related_name='diagnostico', on_delete=models.CASCADE,null=True)
