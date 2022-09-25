from  rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from app.serializers.enfermeroSerializer import EnfermeroSerializer
from datetime import datetime
from app.models import User
from app.serializers.userSerializer import UserSerializer

class ViewsCrearEnfermero(views.APIView):
   
        def post(self, request, *args,**kwargs):
            data_usuario= request.data.pop('usuario_info')
            now = datetime.now()
            data_usuario['create_date']= now.strftime("%Y-%m-%d")
            data_usuario['rol']=User.AplicationRol.ENF
            serializer_user= UserSerializer(data=data_usuario)
            serializer_user.is_valid(raise_exception=True)
            usuario = serializer_user.save()

            data_enfermero = request.data.pop('enfermero_info')
            data_enfermero['usuario']= usuario.id
            data_enfermero['create_date']= now.strftime("%Y-%m-%d")
            serializer_enfermero = EnfermeroSerializer(data=data_enfermero)
            serializer_enfermero.is_valid(raise_exception=True)
            aux = serializer_enfermero.save()

            return Response(status=status.HTTP_201_CREATED)