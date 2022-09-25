from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from app.models.auxiliar import Auxiliar
from app.models.user import User



class AuxiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Auxiliar
        fields=['id','create_date','usuario']

    def create(self, validated_data):
        auxiliarInstance = Auxiliar.objects.create(**validated_data)
        return auxiliarInstance

    def to_representation(self, obj):
        auxiliar= Auxiliar.objects.get(id=obj.id)
        user= User.objects.get(id=auxiliar.usuario.id)
        
        return {
            'auxiliar':{
                'id_auxiliar': auxiliar.id,
                'create_date': auxiliar.craete_date
            },
            'usuario':{
                'id_usuario': user.id,
                'username': user.username,
                'password': user.password,
                'create_date': user.create_date,
                'nombres': user.nombres,
                'apellidos ':user.apellidos, 
                'telefono ':user.telefono,
                'numero_celular ':user.numero_celular,
                'correo':user.correo,
                'tipo_documento':user.tipo_documento,
                'numero_documento':user.numero_documento,
                'direccion':user.direccion,
                'rol':user.rol                
            }
        }