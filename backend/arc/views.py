from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City
from .serializers import CitySerializer


class FullDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        cities = City.objects.all()
        data = CitySerializer(cities, many=True).data
        return Response(data)
