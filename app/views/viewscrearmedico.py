from  rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from app.serializers.medicoSerializer import MedicoSerializer
from datetime import datetime
from app.models import User
from app.serializers.userSerializer import UserSerializer

class ViewsCrearMedico(views.APIView):
   
        def post(self, request, *args,**kwargs):
            data_usuario= request.data.pop('usuario_info')
            now = datetime.now()
            data_usuario['create_date']= now.strftime("%Y-%m-%d")
            data_usuario['rol']=User.AplicationRol.MED
            serializer_user= UserSerializer(data=data_usuario)
            serializer_user.is_valid(raise_exception=True)
            usuario = serializer_user.save()

            data_medico = request.data.pop('medico_info')
            data_medico['usuario']= usuario.id
            data_medico['create_date']= now.strftime("%Y-%m-%d")
            serializer_medico = MedicoSerializer(data=data_medico)
            serializer_medico.is_valid(raise_exception=True)
            aux = serializer_medico.save()

            return Response(status=status.HTTP_201_CREATED)