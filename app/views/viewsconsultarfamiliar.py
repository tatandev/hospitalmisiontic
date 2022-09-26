from  rest_framework import status, views
from rest_framework.response import Response
from app.models import Familiar
from app.serializers.familiarSerializer import Familiarserializers




class ViewsconsultarFamiliar(views.APIView):

    def get(self, request, *args, **kwargs):
                familiar = Familiar.objects.get(id=kwargs['pk'])
                serializer = Familiarserializers(familiar)  
                return Response(serializer.data,status=status.HTTP_200_OK)