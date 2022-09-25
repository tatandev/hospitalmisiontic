from  rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from app.models import Paciente
from app.serializers import pacienteSerializer
from app.serializers.pacienteSerializer import PacienteSerializer




class ViewsconsultarPaciente(views.APIView):

    def get(self, request, pk, format=None):
                paciente = Paciente.objects.get(pk=pk)
                serializer = pacienteSerializer(paciente)  
                return Response(serializer.data)