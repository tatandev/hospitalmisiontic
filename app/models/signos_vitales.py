from django.db import models
from .paciente import Paciente


class Signos_vitales(models.Model):
    id = models.BigAutoField(primary_key=True)
    oximetria = models.CharField(max_length=45)
    frecuencia_respiratoria = models.CharField(max_length=45)
    frecuencia_cardiaca = models.CharField(max_length=45)
    temperatura = models.CharField(max_length=45)
    presion_arterial = models.CharField(max_length=45)
    glicemias = models.CharField(max_length=45)
    fecha_registro = models.DateField()
    paciente = models.ForeignKey(Paciente, related_name='signos_vitales', on_delete=models.CASCADE,null=True)