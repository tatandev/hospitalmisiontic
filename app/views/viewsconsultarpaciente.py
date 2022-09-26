from  rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from app.models import Paciente
from app.serializers import pacienteSerializer
from app.serializers.pacienteSerializer import PacienteSerializer




class ViewsconsultarPaciente(views.APIView):

    def get(self, request, *args, **kwargs):
                paciente = Paciente.objects.get(id=kwargs['pk'])
                serializer = PacienteSerializer(paciente)  
                return Response(serializer.data,status=status.HTTP_200_OK)