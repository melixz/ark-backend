from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City
from .serializers import FullResponseSerializer


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
