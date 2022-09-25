from app.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password','create_date', 'nombres',
         'apellidos', 'telefono', 'numero_celular','correo','tipo_documento',
         'numero_documento','direccion','rol']

        def create(self, validate_data):
            userInstance = User.objects.create(**validate_data)
            return userInstance