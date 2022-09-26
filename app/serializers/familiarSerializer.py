from app.models import familiar
from app.models.familiar import Familiar
from rest_framework import serializers 
from app.models.auxiliar import Auxiliar

class Familiarserializers(serializers.ModelSerializer):
    class Meta:
        model = Familiar 
        fields = ['id', 'nombres', 'apellidos', 'tipo_documento', 'numero_documento', 'direccion', 'telefono', 'numero_celular', 'correo', 'parentezco','auxiliar']

        def create(self, validated_data):
            FamiliarInstance= Familiar.objects.create(**validated_data)
            return FamiliarInstance