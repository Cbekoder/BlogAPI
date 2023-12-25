from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

# class MaqolaModelViewSet(ModelViewSet):
#     queryset = Maqola.objects.all()
#     serializer_class = MaqolaSerializer
#     pagination_class = PageNumberPagination
#     pagination_class.page_size = 3

class MaqolalarAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        maqolalar = Maqola.objects.all().order_by('-sana')
        serializer = MaqolaSerializer(maqolalar, many=True)
        return Response(serializer.data)

    def post(self, reqeust):
        maqola = reqeust.data
        serializer = MaqolaSerializer(data=maqola)
        if serializer.is_valid():
            serializer.save(muallif=reqeust.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

