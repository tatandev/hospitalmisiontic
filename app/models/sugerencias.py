from django.db import models
from .medico import Medico
from .paciente import Paciente

class Sugerencias (models.Model):
    id = models.BigAutoField(primary_key=True)
    sugerencia = models.CharField (max_length = 200 )
    fecha_registro= models.DateField ()
    medico = models.ForeignKey(Medico,related_name='sugerencias', on_delete=models.CASCADE,null=True)
    paciente = models.ForeignKey(Paciente,related_name='sugerencias', on_delete=models.CASCADE,null=True)