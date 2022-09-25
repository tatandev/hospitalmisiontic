from email.policy import default
from django.db import models
from .user import User
from .familiar import Familiar
from .enfermero import Enfermero
from .medico import Medico
from .auxiliar import Auxiliar

class Paciente (models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_nacimiento = models.DateField ()
    departamento = models.CharField (max_length = 45)
    ciudad = models.CharField (max_length = 45)
    estado_civil = models.CharField (max_length = 10)
    ocupacion = models.CharField (max_length = 45)
    etnia = models.CharField (max_length = 45)
    rH = models.CharField (max_length = 10)
    genero = models.CharField (max_length = 10)
    enfermedades_hereditarias = models.CharField (max_length = 10)
    numero_embarazos = models.IntegerField (default = 0)
    numero_abortos = models.IntegerField (default = 0)
    numero_operaciones = models.IntegerField (default = 0)
    create_date = models.DateTimeField ('create_date')
    familiar = models.ForeignKey (Familiar, related_name='paciente', on_delete=models.CASCADE,null=True)
    enfermero = models.ForeignKey (Enfermero, related_name='paciente', on_delete=models.CASCADE,null=True)
    medico = models.ForeignKey (Medico, related_name='paciente', on_delete=models.CASCADE,null=True)
    usuario = models.ForeignKey (User, related_name='paciente', on_delete=models.CASCADE)
    auxiliar = models.ForeignKey (Auxiliar, related_name='paciente', on_delete=models.CASCADE,null=True)