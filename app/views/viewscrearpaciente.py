from  rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from app.serializers.pacienteSerializer import PacienteSerializer
from datetime import datetime
from app.models import User
from app.serializers.userSerializer import UserSerializer

class ViewsCrearPaciente(views.APIView):
   
        def post(self, request, *args,**kwargs):
            data_usuario= request.data.pop('usuario_info')
            now = datetime.now()
            data_usuario['create_date']= now.strftime("%Y-%m-%d")
            data_usuario['rol']=User.AplicationRol.PAC
            serializer_user= UserSerializer(data=data_usuario)
            serializer_user.is_valid(raise_exception=True)
            usuario = serializer_user.save()

            data_paciente = request.data.pop('paciente_info')
            data_paciente['usuario']= usuario.id
            data_paciente['create_date']= now.strftime("%Y-%m-%d")
            serializer_paciente = PacienteSerializer(data=data_paciente)
            serializer_paciente.is_valid(raise_exception=True)
            aux = serializer_paciente.save()

            return Response(status=status.HTTP_201_CREATED)

    