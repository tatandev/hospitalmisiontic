from django.db import models
from .user import User
from .auxiliar import Auxiliar

class Medico (models.Model):
    id = models.BigAutoField(primary_key=True)
    especializacion = models.CharField (max_length = 45)
    rh = models.CharField (max_length = 45)
    create_date = models.DateTimeField ('create_date')
    usuario = models.ForeignKey (User, related_name = 'medico', on_delete = models.CASCADE)
    auxiliar  = models.ForeignKey (Auxiliar, related_name = 'medico', on_delete = models.CASCADE,null=True)