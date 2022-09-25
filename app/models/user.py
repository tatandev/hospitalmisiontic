from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password):
      
        user = self.create_user(
            username=username,
            password=password,
            )
        user.is_admin = True
        user.save(using=self._db)
        return user
        
class User (AbstractBaseUser, PermissionsMixin):

    class AplicationRol(models.TextChoices):
        MED='MEDICO'
        ENF='ENFERMER@'
        PAC='PACIENTE'
        FAM='FAMILIAR'
        AUX='AUXILIAR'


    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length = 45, unique=True)
    password = models.CharField('Password', max_length = 256)
    create_date = models.DateTimeField('create_date')
    nombres = models.CharField('nombres', max_length = 45)
    apellidos = models.CharField('apellidos', max_length=45)
    telefono = models.CharField('telefono', max_length=30)
    numero_celular = models.CharField('numero_celular', max_length=30)
    correo = models.EmailField('correo', max_length=100)
    tipo_documento = models.CharField ('tipo_documento', max_length = 100)
    numero_documento = models.CharField ('numero_documento', max_length = 100)
    direccion = models.CharField ('direccion', max_length = 45)

    rol = models.CharField(
        max_length=45,
        choices=AplicationRol.choices,
        default=AplicationRol.PAC,
    )



 
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'