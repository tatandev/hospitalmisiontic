from django.db import models
from .auxiliar import Auxiliar

class Familiar (models.Model):
    id = models.BigAutoField(primary_key=True)
    nombres = models.CharField (max_length = 45)
    apellidos = models.CharField (max_length = 45)
    tipo_documento = models.CharField (max_length = 45)
    numero_documento = models.CharField (max_length = 25)
    direccion = models.CharField (max_length = 45)
    telefono = models.CharField (max_length = 45)
    numero_celular = models.CharField (max_length = 45)
    correo = models.CharField (max_length = 45)
    parentezco = models.CharField (max_length = 45)
    auxiliar  = models.ForeignKey (Auxiliar, related_name = 'familiar', on_delete = models.CASCADE,null=True)
