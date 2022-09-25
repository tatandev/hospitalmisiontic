from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from app.models import User
from app.models import Paciente
from app.serializers import UserSerializer


class PacienteSerializer (serializers.ModelSerializer):
    class Meta:
        model=Paciente
        fields=['id','fecha_nacimiento','departamento','ciudad',
        'estado_civil','ocupacion','etnia','rH','genero','enfermedades_hereditarias',
        'numero_embarazos','numero_abortos','numero_operaciones','create_date',
        'familiar','enfermero','medico','usuario','auxiliar']

    
    def create(self, validated_data):
        pacienteInstance=Paciente.objects.create(**validated_data)
        return pacienteInstance

    def to_representation(self, obj):
        paciente= Paciente.objects.get(id=obj.id)
        user=User.objects.get(id=paciente.usuario.id)
        
        return {
            'paciente':{
                'id_paciente':paciente.id,
                'fecha_nacimiento':paciente.fecha_nacimiento,
                'departamento':paciente.departamento,
                'ciudad':paciente.ciudad,
                'estado_civil':paciente.estado_civil,
                'ocupacion':paciente.ocupacion,
                'etnia':paciente.etnia,
                'rH':paciente.rH,
                'genero':paciente.genero,
                'enfermedades_hereditarias':paciente.enfermedades_hereditarias,
                'numero_embarazos':paciente.numero_embarazos,
                'numero_abortos':paciente.numero_abortos,
                'numero_operaciones':paciente.numero_operaciones,
                'create_date':paciente.create_date
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