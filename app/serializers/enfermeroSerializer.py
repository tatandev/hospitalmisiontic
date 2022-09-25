from dataclasses import fields
from rest_framework import serializers
from app.models import Enfermero
from app.models import User

class EnfermeroSerializer(serializers.ModelSerializer):

    class Meta: 
        model= Enfermero
        fields= ['id','rh','especialidad','auxiliar','usuario']

    def create(self, validated_data):
        EnfermeroInstance= Enfermero.objects.create(**validated_data)
        return EnfermeroInstance
    
    def to_representation(self, obj):
        enfermero = Enfermero.objects.get(id=obj.id)
        user= User.objects.get(id=enfermero.usuario.id)

        return {
            'enfermero' : {
                'id_enfermero' : enfermero.id,
                'rh' : enfermero.RH,
                'especialidad': enfermero.especialidad        
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
