from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from app.models import Medico, User

class MedicoSerializer (serializers.ModelSerializer):
    class Meta:
        model= Medico
        fields=['id','especializacion','rh','create_date','usuario',
        'auxiliar']

    def create(self, validated_data):
        
        medicoIntance= Medico.objects.create(**validated_data)
        return medicoIntance

    def to_representation(self, obj):
        medico= Medico.objects.get(id=obj.id)
        user =User.objects.get(id=medico.usuarios.id)

        return {
            'medico':{
                'id_medico': medico.id,
                'especializacion': medico.especializacion,
                'rh': medico.rh,
                'create_date': medico.create_date
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