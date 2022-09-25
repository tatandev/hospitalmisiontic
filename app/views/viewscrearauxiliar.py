from datetime import datetime
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from app.models import User, Auxiliar
from app.serializers.auxiliarSerializer import AuxiliarSerializer
from app.serializers.userSerializer import UserSerializer


class ViewsAuxiliarView(views.APIView):

        def post(self, request, *args,**kwargs):
            data_usuario= request.data.pop('usuario_info')
            now = datetime.now()
            data_usuario['create_date']= now.strftime("%Y-%m-%d")
            data_usuario['rol']=User.AplicationRol.AUX
            serializer_user= UserSerializer(data=data_usuario)
            serializer_user.is_valid(raise_exception=True)
            usuario = serializer_user.save()

            data_auxiliar = request.data.pop('auxiliar_info')
            data_auxiliar['usuario']= usuario.id
            data_auxiliar['create_date']= now.strftime("%Y-%m-%d")
            serializer_auxiliar = AuxiliarSerializer(data=data_auxiliar)
            serializer_auxiliar.is_valid(raise_exception=True)
            aux = serializer_auxiliar.save()

            

            return Response(status= status.HTTP_201_CREATED)
