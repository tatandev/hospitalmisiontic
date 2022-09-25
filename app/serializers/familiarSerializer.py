from app.models import familiar
from app.models.familiar import Familiar
from rest_framework import serializers 

class Familiarserializers(serializers.ModelSerializer):
    class Meta:
        model = Familiar 
        fields = ['id', 'nombres', 'apellidos', 'tipo_documento', 'numero_documento', 'direccion', 'telefono', 'numero_celular', 'correo', 'parentezco']

        def create(self, validated_data):
            FamiliarInstance= Familiar.objects.create(**validated_data)
            return FamiliarInstance