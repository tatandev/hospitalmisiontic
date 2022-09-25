from django.db import models
from .user import User

class Auxiliar(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_date = models.DateTimeField('create_date')
    usuario = models.ForeignKey(User,related_name='id_usuario_auxiliar', on_delete=models.CASCADE)