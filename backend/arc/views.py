from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City
from .serializers import FullResponseSerializer, CityDataSerializer


class FullDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        cities = City.objects.all()
        new_cities_data = CityDataSerializer(cities, many=True, context={'request': request}).data
        plots_cities_data = CityDataSerializer(cities, many=True, context={'request': request}).data

        response_data = {
            "new": new_cities_data,
            "plots": plots_cities_data,
        }

        return Response(FullResponseSerializer(response_data).data)
