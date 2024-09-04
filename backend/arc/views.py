from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import City
from .serializers import FullResponseSerializer, ContactRequestSerializer


class FullDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        cities = City.objects.all()
        response_data = {
            "new": cities,
            "plots": cities,
        }
        return Response(
            FullResponseSerializer(response_data, context={"request": request}).data
        )

    def post(self, request, *args, **kwargs):
        serializer = ContactRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Заявка успешно отправлена"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
